#!/usr/bin/env python3
# analyze_domain.py (refined)

import ast
import os
from collections import defaultdict

ROOT = "."
# каталоги, которые надо пропускать
EXCLUDE_DIRS = {
    "venv", ".venv", "__pycache__", ".git", "tests",
    "env", "myenv", "build", "dist", ".eggs", "site-packages"
}

def iter_py_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        # отбросить ветви, содержащие любые исключения
        if any(ex in dirpath.split(os.sep) for ex in EXCLUDE_DIRS):
            continue
        for fn in filenames:
            if fn.endswith(".py"):
                yield os.path.join(dirpath, fn)

def name_from_node(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Subscript):
        return name_from_node(node.value)
    return None

def collect_from_file(path):
    try:
        src = open(path, "r", encoding="utf8").read()
        tree = ast.parse(src, path)
    except Exception:
        return []
    classes = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            cls = {"name": node.name, "fields": set(), "methods": [], "assocs": set(), "is_exception": False}
            # базовые классы
            for b in node.bases:
                bname = name_from_node(b)
                if bname and (bname.endswith("Exception") or bname == "Exception"):
                    cls["is_exception"] = True
            # собрать члены класса
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    if not (item.name.startswith("__") and item.name.endswith("__")):
                        cls["methods"].append(item.name)
                    # параметры и аннотации → ассоциации
                    for arg in item.args.args + item.args.kwonlyargs:
                        if arg.annotation:
                            for n in ast.walk(arg.annotation):
                                if isinstance(n, ast.Name):
                                    cls["assocs"].add(n.id)
                                if isinstance(n, ast.Attribute):
                                    cls["assocs"].add(n.attr)
                    if item.returns:
                        for n in ast.walk(item.returns):
                            if isinstance(n, ast.Name):
                                cls["assocs"].add(n.id)
                elif isinstance(item, ast.Assign):
                    for t in item.targets:
                        if isinstance(t, ast.Name):
                            cls["fields"].add(t.id)
                elif isinstance(item, ast.AnnAssign):
                    t = item.target
                    if isinstance(t, ast.Name):
                        cls["fields"].add(t.id)
            # __init__ — self.x присваивания и аннотации аргументов
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                    for n in ast.walk(item):
                        if isinstance(n, ast.Assign):
                            for t in n.targets:
                                if isinstance(t, ast.Attribute) and isinstance(t.value, ast.Name) and t.value.id == "self":
                                    cls["fields"].add(t.attr)
                        if isinstance(n, ast.AnnAssign):
                            t = n.target
                            if isinstance(t, ast.Attribute) and isinstance(t.value, ast.Name) and t.value.id == "self":
                                cls["fields"].add(t.attr)
                        for arg in item.args.args:
                            if arg.arg != "self" and arg.annotation:
                                for m in ast.walk(arg.annotation):
                                    if isinstance(m, ast.Name):
                                        cls["assocs"].add(m.id)
            # простая эвристика по строковым literal‑аннотациям
            for n in ast.walk(node):
                if isinstance(n, ast.Constant) and isinstance(n.value, str):
                    txt = n.value
                    # вычленить слова, начинающиеся с заглавной буквы
                    for token in txt.replace("(", " ").replace(")", " ").split():
                        if token and token[0].isupper():
                            cls["assocs"].add(token.strip(",:"))
            classes.append(cls)
    return classes

def analyze(root):
    package_stats = defaultdict(lambda: {"classes":0, "fields":0, "methods":0, "assocs":0, "exceptions":0})
    total = {"classes":0, "fields":0, "methods":0, "assocs":0, "exceptions":0}
    for path in iter_py_files(root):
        rel = os.path.relpath(path, root)
        parts = rel.split(os.sep)
        pkg = parts[0] if len(parts) > 1 else "_root"
        classes = collect_from_file(path)
        for c in classes:
            package_stats[pkg]["classes"] += 1
            package_stats[pkg]["fields"] += len(c["fields"])
            package_stats[pkg]["methods"] += len(c["methods"])
            package_stats[pkg]["assocs"] += len(c["assocs"])
            if c["is_exception"]:
                package_stats[pkg]["exceptions"] += 1
            total["classes"] += 1
            total["fields"] += len(c["fields"])
            total["methods"] += len(c["methods"])
            total["assocs"] += len(c["assocs"])
            if c["is_exception"]:
                total["exceptions"] += 1
    return package_stats, total

def format_readme(stats, total):
    lines = []
    for pkg in sorted(stats):
        v = stats[pkg]
        lines.append(f"{pkg}: classes={v['classes']}, fields={v['fields']}, methods={v['methods']}, assocs={v['assocs']}, exceptions={v['exceptions']}")
    lines.append("")
    lines.append("Total:")
    lines.append(str(total))
    return "\n".join(lines)

if __name__ == "__main__":
    pkgs, tot = analyze(ROOT)
    print(format_readme(pkgs, tot))

class ArtStyle:
    def __init__(self, name: str, description: str = "", origin_year: int = None, typical_features: list = None):
        self.name = name
        self.description = description
        self.origin_year = origin_year if origin_year is not None else 0
        self.typical_features = typical_features or []

    def short_description(self) -> str:
        return f"{self.name}: {self.description[:80]}"

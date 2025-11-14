# Тесты для класса FinancialReport

from finance.FinancialReport import FinancialReport

class DummyDirector: pass

def test_generate_pdf_and_send():
    rep = FinancialReport("Q1-2025", "data")
    pdf = rep.generate_pdf()
    assert "PDF generated" in pdf
    assert rep.send_to_director(DummyDirector()) is True

import pytest

from src.category import Category


@pytest.fixture
def category_init():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни",
        [],
    )


def test_category_init(category_init):
    assert category_init.name == "Смартфоны"
    assert (
        category_init.description
        == "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category_init.products == []

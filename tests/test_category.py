import pytest

from src.category import Category


def test_category_init(category_init):
    assert category_init.name == "Смартфоны"
    assert (
        category_init.description
        == "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category_init.products == []

def test_category(
    category1,
    product1,
    product3,
    product2,
    category2,
    product4,
    category3,
):
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category1.products == [product1, product2, product3]

    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category2.products == [product1]

    assert category3.name == "Телевизоры"
    assert (
        category3.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category3.products == [product4]

    assert len(category1.products) == 3
    assert len(category2.products) == 1
    assert len(category3.products) == 1

    assert category1.category_count == 4
    assert category2.category_count == 4
    assert category3.category_count == 4

    assert category1.products_count == 5
    assert category2.products_count == 5
    assert category3.products_count == 5
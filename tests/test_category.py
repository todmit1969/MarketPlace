from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
import pytest


def test_category_1(category1):
    category1.category_count = 1
    product = []
    product.append(category1.products)
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(product) == 1


def test_category_2(category1, category2):
    assert category1.category_count == 3
    assert category2.products_count == 7
    assert category1.products_count == 7


def test_add_new_product(category1):
    old_count = len(category1.products)
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1.add_product(product)
    expected_count = old_count + 1
    assert len(category1.products) == expected_count


def test_category_str(category1):
    assert (
        str(category1) == "Название категории: Смартфоны, количество продуктов: 27 шт."
    )


def test_product_len_price(product1, product2, product3):
    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )
    assert category1.middle_price() == 19000.0

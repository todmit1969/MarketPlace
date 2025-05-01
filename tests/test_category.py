from src.product import Product
from src.smartphone import Smartphone
import pytest

def test_category_1(category1):
    category1.category_count = 1
    product = []
    product.append(category1.products)
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(product) == 1


def test_category_2(category1, category2):
    assert category1.category_count == 3
    assert category2.products_count == 7
    assert category1.products_count == 7

def test_products_list(category1, category2):
    # assert first_category.products == 'Смартфоны, количество продуктов: 5'
    # assert second_category.products == 'Телевизоры, количество продуктов: 7'
    print(category1.products)
    print(category2.products)

def test_add_new_product(category1):
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1.add_product(product)
    assert category1.products == [
                                    Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5),
                                    Product('Iphone 15', '512GB, Gray space', 210000.0, 8),
                                    Product('55 QLED 4K', 'Фоновая подсветка', 123000.0, 14),
                                    Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
                                ]

def test_category_str(category1):
    assert str(category1) == "Название категории: Смартфоны, количество продуктов: 27 шт."

def test_add_new_product_2(category1):
    product = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    category1.add_product(product)
    assert category1.products == [
                                    Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5),
                                    Product('Iphone 15', '512GB, Gray space', 210000.0, 8),
                                    Product('55 QLED 4K', 'Фоновая подсветка', 123000.0, 14),
                                    Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
                                ]

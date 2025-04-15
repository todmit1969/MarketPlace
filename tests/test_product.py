import pytest

from src.product import Product


@pytest.fixture
def product_init():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, "
                                    "200MP камера", 180000.0, 5
    )


def test_product_init(product_init):
    assert product_init.name == "Samsung Galaxy S23 Ultra"
    assert product_init.description == "256GB, Серый цвет, 200MP камера"
    assert product_init.price == 180000.0
    assert product_init.quantity == 5

def tests_products(product1, product2, product3, product4):
    assert product1.name == "Samsung"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8

    assert product3.name == "55 QLED 4K"
    assert product3.description == "Фоновая подсветка"
    assert product3.price == 123000.0
    assert product3.quantity == 7

    assert product4.name == "Xiaomi Redmi Note 11"
    assert product4.description == "1024GB, Синий"
    assert product4.price == 31000.0
    assert product4.quantity == 14

def test_product_str(product_str):
    assert str(product_str) == "Название продукта: Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

def test_product_add(product1, product2):
    assert print(product1 + product2) == 2580000.0
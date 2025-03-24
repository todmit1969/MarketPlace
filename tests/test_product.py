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

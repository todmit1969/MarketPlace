import pytest

from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_products(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_price_property(product1):
    assert product1.price == 180000.0

def test_new_product():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_product_str(product1):
    assert str(product1) == "Название продукта: Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product1, product2):
    assert product1+product2 == 2580000.0


def test_smartphone(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_grass(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1+smartphone2 == 2580000.0


def test_smartphone_wrong_add(smartphone1, grass1):
    with pytest.raises(TypeError):
        result = smartphone1 + 1


def test_grass_add(grass1, grass2):
    assert grass1 + grass2 == 16750.0


def test_mixinprint(capsys):
    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"

def test_product_invalid_raises_value_error():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        # Создаём объект Product с нулевым количеством, чтобы проверить выброс исключения
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)

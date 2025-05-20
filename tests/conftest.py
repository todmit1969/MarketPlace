import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


@pytest.fixture
def category_init():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни",
        [],
    )


@pytest.fixture
def product1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def product2():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


@pytest.fixture
def product3():
    return Product(
        name="55 QLED 4K",
        description="Фоновая подсветка",
        price=123000.0,
        quantity=14)


@pytest.fixture
def product4():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def category1(product1, product2, product3):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
        products=[product1, product2, product3],
    )


@pytest.fixture
def category2(product1, product2):
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться"
                    " просмотром, станет вашим другом и помощником",
        products=[product1],
    )


@pytest.fixture
def category3(product4):
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет "
                    "наслаждаться просмотром, станет вашим другом и помощником",
        products=[product4],
    )


@pytest.fixture
def product_str():
    return "Название продукта: Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

@pytest.fixture
def smartphone1():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space"
    )


@pytest.fixture
def grass1():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )


@pytest.fixture
def grass2():
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый"
    )

@pytest.fixture
def product_invalid():
    # Здесь создаётся объект Product, который должен вызвать исключение
    return Product("Бракованный товар", "Неверное количество", 0.0, 0)
from src.product import Product
from src.smartphone import Smartphone


def test_category_1(category1):
    category1.category_count = 1
    product = []
    product.append(category1.products)
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(product) == 1


def test_category_2(category1, category2):
    assert category1.category_count == 3
    assert category2.products_count == 3
    assert category1.products_count == 3

def test_products_list(category1, category2):
    # assert first_category.products == 'Смартфоны, количество продуктов: 5'
    # assert second_category.products == 'Телевизоры, количество продуктов: 7'
    print(category1.products)
    print(category2.products)


def test_add_new_product(category1):
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1.add_product(product)
    assert category1.products == ('Iphone 15, 210000.0 руб., Остаток: 8 шт.\n'
                                       'Xiaomi Redmi Note 11, 31000.0 руб., Остаток: 14 шт.')


def test_category_str(category1):
    assert str(category1) == "Название категории: Смартфоны, количество продуктов: 27 шт."


def test_add_new_product_2(category1):
    product = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    category1.add_product(product)
    assert category1.products == ("Iphone 15, 210000.0 руб., Остаток: 8 шт.\n"
                                    "Xiaomi Redmi Note 11, 31000.0 руб., Остаток: 14 шт.")
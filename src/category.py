from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    products_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.products_count += len(products) if products else 0

    def __str__(self):
        products_qty = sum(product.quantity for product in self.__products)
        return (f"Название категории: {self.name},"
                f" количество продуктов: {products_qty} шт.")

    @property
    def products(self):
        return self.__products

    def add_product(self, product):
        if isinstance(product, Product) or issubclass(product, Product):
            self.__products.append(product)
            Category.products_count += 1
        else:
            print("Неверный формат данных!")

    def middle_price(self):

        try:
            total_price = sum([product.price for product in self.__products])
            total_qty = sum([product.quantity for product in self.products])
            return  round(total_price / total_qty, 2)

        except ZeroDivisionError:
            return 0
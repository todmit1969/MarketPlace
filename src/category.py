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

    @property
    def products(self):
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products])

    def add_product(self, product):
        self.__products.append(product)
        Category.products_count += 1

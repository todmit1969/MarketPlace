class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"Product(name={self.name}, "
            f"description={self.description}, "
            f"price={self.price}, "
            f"quantity={self.quantity})"
        )
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        elif new_price <= 0:
            print("Цена не может быть отрицательной или равна нулю!")

    @classmethod
    def new_product(cls, dict_products):
        name = dict_products['name']
        description = dict_products['description']
        price = dict_products['price']
        quantity = dict_products['quantity']

        new_products = Product(name, description, price, quantity)
        return new_products

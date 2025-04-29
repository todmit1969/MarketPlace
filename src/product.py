from src.baseproduct import BaseProduct
from src.mixinprint import MixinPrint

class Product(MixinPrint, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
         #(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()


    def __str__(self):
        return (f"Название продукта: {self.name}, "
                f"{self.__price} руб. Остаток: {self.quantity} шт.")

    def __add__(self, other):
        if isinstance(other, Product) or issubclass(other, Product):
            return ((self.__price * self.quantity) +
                    (other.__price * other.quantity))
        return NotImplemented

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
        if dict_products['quantity'] <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен!")
        else:
            quantity = dict_products['quantity']



        new_products = Product(name, description, price, quantity)
        return new_products

from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self):
        """ Геттер для цены """
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        """ Сеттер для цены с проверкой """
        pass

    @abstractmethod
    def new_product(cls, dict_products):
        pass
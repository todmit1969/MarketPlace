from abc import ABC, abstractmethod


class BaseProduct(ABC):

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
from src.product import Product


class LawnGrass(Product):

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, dict_lawngrass):
        name = dict_lawngrass["name"]
        description = dict_lawngrass["description"]
        price = dict_lawngrass["price"]
        quantity = dict_lawngrass["quantity"]
        country = dict_lawngrass["country"]
        germination_period = dict_lawngrass["germination_period"]
        color = dict_lawngrass["color"]

        new_lawngrass = LawnGrass(
            name, description, price, quantity, country, germination_period, color
        )
        return new_lawngrass

class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"Product(name={self.name}, "
            f"description={self.description}, "
            f"price={self.price}, "
            f"quantity={self.quantity})"
        )

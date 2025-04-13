class Category:
    name: str
    description: str
    products: list
    products_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.products_count += len(products) if products else 0

        def add_product(self, product):
            self.products.append(product)
            Category.products_count += 1

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, description={self.description}, price={self.price})"
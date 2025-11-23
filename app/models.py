class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, description={self.description}, price={self.price})"

    @classmethod
    def get_all_products(cls):
        """Return a list of all available products"""
        products = [
            cls("Laptop", "High-performance laptop for professionals", 999.99),
            cls("Wireless Mouse", "Ergonomic wireless mouse with precision tracking", 29.99),
            cls("USB-C Cable", "Durable USB-C charging cable, 6ft", 12.99),
            cls("Mechanical Keyboard", "RGB mechanical gaming keyboard", 79.99),
            cls("Monitor Stand", "Adjustable monitor stand for dual displays", 49.99),
            cls("Webcam", "1080p HD webcam with noise-cancelling mic", 59.99),
            cls("LED Desk Lamp", "Adjustable LED desk lamp with USB charging port", 39.99),
            cls("Laptop Backpack", "Water-resistant laptop backpack with multiple compartments", 79.99),
        ]
        return products
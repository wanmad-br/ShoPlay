class Product:
    def __init__(self, item_id, name, description, price, category, rarity, stock):
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.rarity = rarity
        self.stock = stock

    def __repr__(self):
        return (
            f"Product(id={self.id}, name={self.name}, category={self.category}, "
            f"rarity={self.rarity}, price={self.price}, stock={self.stock})"
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'rarity': self.rarity,
            'stock': self.stock,
        }

    @classmethod
    def get_all_products(cls):
        """Return the fantasy inventory for the virtual shop."""
        products = [
            cls(1, "Iron Sword", "A balanced blade forged for brave adventurers.", 120.00, "Weapon", "Common", 12),
            cls(2, "Moonlit Cape", "A shimmering cape that hides your steps beneath the stars.", 85.00, "Armor", "Rare", 9),
            cls(3, "Flame Orb", "An enchanted orb that flickers with simmering fire.", 150.00, "Relic", "Epic", 6),
            cls(4, "Crystal Shield", "A defensive wall that deflects the harshest blows.", 200.00, "Armor", "Epic", 4),
            cls(5, "Storm Bow", "A powerful bow that launches arrows with thunderous force.", 175.00, "Weapon", "Rare", 7),
            cls(6, "Shadow Dagger", "A stealth weapon crafted for rapid strikes.", 95.00, "Weapon", "Uncommon", 14),
            cls(7, "Dragonhide Boots", "Boots lined with scales that resist flame and dust.", 110.00, "Armor", "Rare", 10),
            cls(8, "Arcane Wand", "A wand humming with magical energy and ancient glyphs.", 130.00, "Relic", "Epic", 5),
        ]
        return products
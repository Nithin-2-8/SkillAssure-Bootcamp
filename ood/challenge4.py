class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    # Total number of menu items
    def get_total_items(self):
        return len(self.items)

    # List items by course category
    def get_items_by_category(self, category):
        return [item.name for item in self.items if item.category == category]

class SpecialMenu(Menu): # Inheritance
    # This class represents the 30% discount menu
    def get_discounted_price(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item.price * 0.70 # 30% off
        return None

def main():
    menu = Menu()
    menu.add_item(MenuItem("Spring Roll", 5.0, "Appetizer"))
    menu.add_item(MenuItem("Steak", 20.0, "Main"))
    menu.add_item(MenuItem("Ice Cream", 4.0, "Dessert"))

    # Create a special menu (30% off) and copy items
    special = SpecialMenu()
    for it in menu.items:
        special.add_item(it)

    print(f"Total menu items: {menu.get_total_items()}")
    print("Appetizers:", menu.get_items_by_category("Appetizer"))
    print("Mains:", menu.get_items_by_category("Main"))
    print("Desserts:", menu.get_items_by_category("Dessert"))

    # Example: show discounted price for Ice Cream
    item_name = "Ice Cream"
    discounted = special.get_discounted_price(item_name)
    if discounted is not None:
        print(f"Discounted price for {item_name}: {discounted:.2f}")
    else:
        print(f"{item_name} not found in special menu")


if __name__ == '__main__':
    main()
class Ship:
    def __init__(self, name):
        self.name = name
        self.revenue = 0

    def collect_money(self, amount):
        self.revenue += amount

class CruiseShip(Ship):
    def __init__(self, name):
        super().__init__(name)
        self.passengers = []

    def register_passenger(self, customer, ticket_price):
        self.passengers.append(customer)
        self.collect_money(ticket_price)

class Company:
    def __init__(self):
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    # Query 1: Total amount collected (across all ships)
    def get_total_revenue(self):
        return sum(ship.revenue for ship in self.ships)

    # Query 2: List total amount for every ship
    def print_ship_revenues(self):
        for ship in self.ships:
            print(f"{ship.name}: ${ship.revenue}")

# Usage
titanic = CruiseShip("Titanic")
titanic.register_passenger("Jack", 500)

mary = Ship("Mary Cargo") # Generic or CargoShip
mary.collect_money(5000)

company = Company()
company.add_ship(titanic)
company.add_ship(mary)

print(f"Total Revenue: {company.get_total_revenue()}")
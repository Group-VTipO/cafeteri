from customer import Customer
class Menu:
    def __init__(self):
        self.items = {}
        self.customers = []

    def add_item(self, name=None, price=None, details=None):
        self.items[name] = {
            'name': name,
            'price': price,
            'details': details
        }

    def remove_item(self, name):
        del self.items[name]

    def get_items(self):
        return self.items

    def get_item(self, name):
        return self.items.get(name)

    def add_customer(self, name, email, phone_number, address):
        customer = Customer(name, email, phone_number, address, self)
        self.customers.append(customer)

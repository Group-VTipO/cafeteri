class Customer:
    def __init__(self, name, email, phone_number, address, menu):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.menu = menu
        self.order = []

    def get_contact_info(self):
        return f"{self.name}, {self.email}, {self.phone_number}, {self.address}"

    def add_to_order(self, item_name):
        item = self.menu.get_item(item_name)
        if item:
            self.order.append(item)

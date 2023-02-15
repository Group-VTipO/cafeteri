class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, description):
        self.items[name] = {
            'price': price,
            'description': description
        }

    def remove_item(self, name):
        del self.items[name]

    def get_items(self):
        return self.items


# обьект
menu = Menu()

# внесение меню в Объект
menu.add_item('Cappuccino', 3.50, 'Эспрессо со взбитым молоком')
menu.add_item('Latte', 4.00, 'Эспрессо с вспененным молоком')
menu.add_item('Mocha', 4.50, 'Эспрессо с шоколадом и вспененным молоком')
menu.add_item('Moxito', 3.00, 'Со льдом и лимоном')

# Получить текущие пункты меню
items = menu.get_items()

# Print menu vse
for name, data in items.items():
    print(name)
    print('-' * len(name))
    print('Price: ${:.2f}'.format(data['price']))
    print(data['description'])
    print()

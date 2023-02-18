from menu import Menu


#  класса Menu
menu = Menu()

# элементы меню
menu.add_item('Cappuccino', 3.50, 'Эспрессо со взбитым молоком')
menu.add_item('Latte', 4.00, 'Эспрессо с вспененным молоком')
menu.add_item('Moxito', 3.00, 'Со льдом и лимоном')

# Добавьте клиента
menu.add_customer("Artykbaev Nurasyl", "nurasyl@example.com", "+77775556633", "2 korpus Enu")

# Получить текущие пункты меню
items = menu.get_items()

# Распечатать меню
for name, data in items.items():
    print(name)
    print('-' * len(name))
    print('Price: ${:.2f}'.format(data['price']))
    print(data['details'])
    print()

# Получить клиента по имени
customer = menu.customers[0]

# Добавьте пункты к заказу клиента
customer.add_to_order('Cappuccino')
customer.add_to_order('Moxito')

# Распечатать заказ клиента
print(f"{customer.name}'s order:")
print(menu.customers[0].get_contact_info())
for item in customer.order:
    print(item['name'], '${:.2f}'.format(item['price']))


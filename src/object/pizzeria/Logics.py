from object.pizzeria.Pizzas_list import *


while True:
    print(f'Hello.\n'
          f'Enter 0 -> Exit\n'
          f'Enter 1 -> All pizzas\n'
          f'Enter 2 -> Pizza price\n'
          f'Enter 3 -> Order')
    client = input('\nYour choise: ')
    match client:
        case '0':
            break
        case '1':
            pizzas.enter()
        case '2':
            pizzas.pizza_price_range()
        case '3':
            pizzas.check()
        case _:
            print('Wrong choice, look in the program menu "Exchanger"')

print('SERVICE STOPPED')














from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
menu_item = MenuItem(name='name', water='water', milk='milk', coffee='coffee', cost='cost' )
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


is_on = True
while is_on:
    user_choice = input(f'What would you like? {menu.get_items()}: ').lower()

    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "":
        print('Please choose correct name!')
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost) and coffee_maker.is_resource_sufficient(drink):
                coffee_maker.make_coffee(drink)


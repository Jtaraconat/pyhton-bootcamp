#objectname = ClassName()
#import turtle
# from turtle import Turtle, Screen #import class Turtle, Screen from module
# timmy = Turtle() #new turtle object from class Turtle in module turtle
# timmy.shape("turtle")
# timmy.color("chartreuse2", "chartreuse4")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight) #print attribute canvheight from my_screen object
# my_screen.exitonclick() #run method exitonclick from my_screen object

#ADD PACKAGES
# find a package on pypi.org
#in terminal py -m pip install -U prettytable

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water","Fire"])
# table.align = "l"
# print(table)


#OOP COFFEE MACHINE
# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine

# my_coffee_maker = CoffeeMaker()
# my_menu = Menu()
# my_money_machine = MoneyMachine()

# is_on = True

# while is_on:
#     options = my_menu.get_items()
#     choice = input(f"what would you like? {options}: ")
    
#     if choice == "off":
#         is_on = False
#     elif choice =="report":
#        my_coffee_maker.report()
#        my_money_machine.report()
#     else:
#         drink = my_menu.find_drink(choice)
#         if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
#             my_coffee_maker.make_coffee(drink)




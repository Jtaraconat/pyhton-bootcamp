#FUNCTION WITH OUTPUTS
# def my_function():
#     return 3 * 2

# output = my_function() => output = 3 * 2

# def format_name(firstname, lastname):
#     if firstname == "" or lastname == "":
#         return "no input valid"
#     formated_firstname = firstname.title()
#     formated_lastname = lastname.title()
#     return f"{formated_firstname} {formated_lastname}"

# formated_string = format_name("JohAn", "TaraCONAt")
# print(formated_string)

#DAYS IN MONTH CHALLENGE
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and is_leap_year(year):
#         return 29
#     else :
#         return month_days[month - 1]

# year = int(input("year"))
# month = int(input("month"))
# days = days_in_month(year, month)
# print(days)


#DOCSTRINGS help to know what a function do in the IDE on mouseover, need """ """ and need to be on firstline 
# def format_name():
#     """this is the documentation for this function"""

#CALCULATOR PROGGRAM
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-" : substract,
    "*" : multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_input = input(f"Type y to continue with the previous answer : {answer}, type n to start a new calculation or type q to quit \n")
        if user_input == "y":
            num1 = answer
        elif user_input == "n":
            should_continue = False
            calculator()
        elif user_input == "q":
            should_continue = False
         

calculator()


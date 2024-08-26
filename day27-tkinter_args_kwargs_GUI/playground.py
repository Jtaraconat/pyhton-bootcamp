from typing import Any


def add(*args):
    #can acces a specific args with args[0] for exemple

    result = 0
    for n in args:
        result += n
    print(result)

add(5,5,5,5,5)


def calculate(n, **kwargs):
    #kwargs create a dictionary, represent argument and value as key/value pair
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=4, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model") #use get(), if key doesn't exist when function is called it will return None and not an error

my_car = Car(make="Nissan")
print(my_car.color)
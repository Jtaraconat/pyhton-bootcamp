#FUNCTION WITH PARAMETERS AND ARGUMENTS

# def greet():
#     print("hello")
#     print("world")
#     print("!")
# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")

# greet_with_name("Jojo")

#Multiple inputs
# def greet_with(name, location):
#      print(f"Hello {name}")
#      print(f"What is it like in {location}?")

# greet_with("Johan", "Toulouse")

#Keywords arguments
# greet_with(location="Toulouse", name="Jojo")


#CHALLENGE PAINT AREA CALCULATOR
# import math
# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {number_of_cans} cans")


# test_h = int(input("height"))
# test_w = int(input("width"))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


#PRIME NUMBER CHECK
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("Prime")
#     else:
#         print("Not prime")

# n = int(input("number"))
# prime_checker(n)


#CHALLENGE CEASAR CIPHER
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True


def ceasar(text, shift, cipher_direction):
    end_text=""
    shift = shift % 26
    if cipher_direction == "decode":
        shift  *= -1 
    for char in text:
        if char in alphabet:
            letter_index = alphabet.index(char)
            new_letter = letter_index + shift
            end_text += alphabet[new_letter]
        else:
            end_text += char

    print(f"{cipher_direction}d text is {end_text}")


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)

    result = input("Type 'yes' if you wnat to continue, otherwise type 'no'\n")
    if result == "no":
        should_continue = False
        print("Goodbye")




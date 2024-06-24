#RANDOMIZATION AND PYTHON LISTS
#need to import 
import random
#import a custom module
# import my_module

#random number between 2 values included
# random_integer = random.randint(1, 10)
# print(random_integer)

#call from custom module
# print(my_module.pi)

#float between 0.0 and 1.0 not included
# random_float = random.random()
# print(random_float)

# #print random between 0 and 5
# random_float2 = (random.random() * 5)
# print(random_float2)

#random toss challenge
# random_int = random.randint(0, 1)
# if(random_int == 0):
#     print("Tails")
# else:
#     print("Heads")

# PYTHON LISTS
#list = [item1, item2]
states_of_america = ["Delaware", "Pennsylvania"]
# print(states_of_america[0])
#get from the end of the list
#print(states_of_america[-1])

#change the value at index 0
# states_of_america[0] = "Pencilvania"
# print(states_of_america)

#add to list
# states_of_america.append("Angelaland")
# print(states_of_america)

#extend a list, add a list to the end of a list
# states_of_america.extend(["Jojoland", "Kakoland"])
# print(states_of_america)

#LIST CHALLENGE
# names_string = "Angela, Ben, Jenny, Michael, Chloe"
# names = names_string.split(", ")
# random_int = random.randint(0, len(names) - 1)
# selected_person = names[random_int]
# print(f"{selected_person} is going to buy the meal today")

#Watch out for out of range list, while using len() and index is based 0

#LIST AND NESTED LIST
#dirty_dozen = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes", "Spinach", "Kale" ]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Tomatoes", "Celery", "Potatoes", "Spinach", "Kale"]
# dirty_dozen = [fruits, vegetables]

#MAP CHALLENGE
# line1 = ["[]", "[]", "[]"]
# line2 = ["[]", "[]", "[]"]
# line3 = ["[]", "[]", "[]"]
# map = [line1, line2, line3]
# print("Hiding your treasure, X mark the spot")
# user_input = input()

# letter = user_input[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)

# number_index = int(user_input[1]) - 1

# map[number_index][letter_index] = "X"

# print(f"{line1}\n{line2}\n{line3}")


#DAY 4 PROJECT ROCK, PAPER, SCISSORS
# user_choice = int(input("What do you choose? type 0 for Rock, type 1 for Paper or 2 for Scissors\n"))
# choices = ["Rock" , "Paper", "Scissors"]
# computer_choice = random.randint(0, 2)
# print(f"Computer chose {choices[computer_choice]}")
# print(f"You chose {choices[user_choice]}")

# if user_choice >= 3 or user_choice < 0:
#     print("You type an invalid number, you lose")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw")

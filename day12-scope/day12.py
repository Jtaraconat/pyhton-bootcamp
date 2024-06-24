# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"inside function {enemies}")

# increase_enemies()
# print(f"outside function {enemies}")


#LOCAL SCOPE
# def drink_potion():
#     strength = 2
#     print(strength)

# drink_potion()
# print(strength) #not defined outside function


#GLOBAL SCOPE
# player_health = 10 #available everywhere
# def drink_potion():
#     strength = 2
#     print(player_health)

# drink_potion()

#applicable for function
# def game():
#     def drink_potion():
#         strength = 2
#         print(player_health)
#     drink_potion() #can call inside scope

# drink_potion() #can't call here


#No bloc scope, in loop, if statement etc...
# game_level = 3
# enemies = ["skeleton", "zombies", "aliens"]

# if game_level > 5:
#     new_enemy = enemies[0]

# print(new_enemy)


#modifying glocal variable
#generally don't want to modify a global variable in a function
# enemies = 1

# def increase_enemies():
#     #global enemies #explicitally specify this is the global variable we want to update
    
#     print(f"inside function {enemies}")
#     return enemies + 1 #can return the updated value

# increase_enemies()
# print(f"outside function {enemies}")


#Global constants: define and don't want to change, write in uppercase
# PI = 3.14159
# URL = "https://www.google.com"


#NUMBER GUESSING GAME
import random

EASY_LEVEL = 10
HARD_LEVEL = 5
turns = 0


def check_answer(guess, answer, turns):
    if guess < answer:
        print("too low")
        return turns - 1
    elif guess > answer:
        print("too high")
        return turns - 1
    else:
        print(f"you got it, the answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. type easy or hard: ")
    if level == "easy":
        return  EASY_LEVEL
    else:
       return HARD_LEVEL
    
def game():
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"you lose the answer was {answer}")
            return 
        elif guess != answer:
            print("guess again")

game()
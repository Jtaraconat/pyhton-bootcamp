############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): #i stops at 19
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) #index out of range, 6 not in index
# print(dice_imgs[dice_num])

# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: #1994 not included in either condition
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") #input not an int
# if age > 18:
# print("You can drive at age {age}.") #indentation error with print statement

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) #comparaison not assignement
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) #indentation error, executing append one time on last loop
#   print(b_list)

# mutate([1,2,3,5,8,13])

#DEBUGGING EXERCISE
# number = int(input("number"))

# if number % 2 = 0: #assignement not comparaison
#     print("stuff")
# else:
#     print("more stuff")
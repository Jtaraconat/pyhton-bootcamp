#if condition:
    #do this
#else:
    #do this

# print("Welcome to the rollercoaster")
# height=int(input("What is your height in cm?"))

# if height > 120:
#     print("You can ride")
# else:
#     print("Sorry you can't ride")

# value = int(input("Number to check"))
# if value % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

#nested if else
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cms ?"))

# if height >= 120:
#     age = int(input("How old are you?"))
#     if age >= 18:
#         print("you can ride and have to pay 12€")
#     else:
#         print("You ca ride and have to pay 7€")
# else:
#     print("Sorry not tall enough")    



#IF ELIF ELSE
# if condition1:
#     do a 
# elif condition b:
#     do b 
# else:
#     do c

# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cms ?"))
# if height >= 120:
#     age = int(input("How old are you?"))
#     if age < 12:
#         print("please pay 5€")
#     elif age <= 18:
#         print("please pay 7€")
#     else:
#         print("please pay 12€")
# else:
#     print("Sorry not tall enough") 


#CODING CHALLENGE BMI 2.0
# height = float(input("What is your height in meters?"))
# weight = int(input("What is your weight in kgs?"))
# bmi = int(weight / (height**2))
# if bmi <= 18.5:
#     print("underweight")
# elif bmi <= 25:
#     print("normal weight")
# elif bmi <= 30:
#     print("slightly overweight")
# elif bmi <= 35:
#     print("obese")
# else:
#     print("clinically obese")

#CODING CHALLENGE LEAP YEAR
# year = int(input("year to test"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")    

# else:
#     print("not leap year")    


#MULTIPLE IF STATEMENT TO EXECUTE MULTIPLE BLOC

# height = int(input("What is your height?\n"))
# bill = 0
# if height >= 120:
#     age = int(input("How old are you?\n"))
#     if age <= 12:
#         bill = 5
#         print(f"ticket is {bill}\n")

#     elif age <= 18:
#         bill = 7
#         print(f"ticket is {bill}\n")

#     else:
#         bill = 12
#         print(f"ticket is {bill}\n")

#     wants_photo = input("Do you want a photo? answer yes or no\n")
#     if wants_photo == "yes":
#         bill += 3
        
#     print(f"Your final bill is {bill}")
     
# else:
#     print("Sorry grow up")    

#PIZZA CHALLENGE
# print("Thank you for choosing pyhon pizza ")
# bill = 0
# size = input("What size do you want? S, M, L?")
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else :
#     bill += 25


# add_pepperoni = input("Do you wanty pepperoni? Y or N?")
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# else:
#     bill = bill

# extra_cheese = input("Do youu want extra cheese? Y or N?")
# if extra_cheese == "Y":
#     bill += 1
# 
# print(f"Your total bill is: {bill}")

#LOGICAL OPERATORS
#AND OR NOT
#condition A and B both must be true => a > 10 and a < 13
#condition A or B one need to be true => a > 10 or a < 13
#NOT reverse condition => not a > 15

# height = int(input("What is your height?\n"))
# bill = 0
# if height >= 120:
#         age = int(input("How old are you?\n"))
#         if age <= 12:
#          bill = 5
#          print(f"ticket is {bill}\n")

#         elif age <= 18:
#          bill = 7
#          print(f"ticket is {bill}\n")

#         elif age >= 45 and age <=55:
#          print(f"ticket is {bill}\n")

#         wants_photo = input("Do you want a photo? answer yes or no\n")
#         if wants_photo == "yes":
#          bill += 3
# print(f"Your final bill is {bill}")

# print("the love calculator is calculating your score")
# name1 = input("What is your name ")
# name2= input("Whate is their name")
# combined_names = name1 + name2
# lowered_names = combined_names.lower()
# t = lowered_names.count("t")
# r = lowered_names.count("r")
# u = lowered_names.count("u")
# e = lowered_names.count("e")
# first_digit = t + r + u + e
# print(first_digit)

# l = lowered_names.count("l")
# o = lowered_names.count("o")
# v = lowered_names.count("v")
# e = lowered_names.count("e")
# second_digit = l + o + v + e
# print(second_digit)

# love_score = int(str(first_digit) + str(second_digit))
# print(love_score)

# if(love_score < 10 or love_score > 90):
#     print(f"your score is {love_score} you go together like coke and mentos")
# elif(int(love_score) >= 40 and love_score <= 50 ):
#     print(f"your score is {love_score} you are alright together")
# else:
#     print(f"your score is {love_score}")


#FINAL PROJECT
print("Welcome to treasure island")
print("Your mission is to find the treasure")
left_right = input("Do you want to go left or right? type left or right\n")
if(left_right == "left"):
    swim_wait = input("You arrived in front of a lake do you want to swim or wait for the boat? type swim or boat\n")
    if(swim_wait =="wait"):
        color_house = input("you waited. you now arrived in front of three houses one blue, one red and one yellow. Whiwh house do you open? type blue yellow or red\n")
        if(color_house == "blue" or color_house == "red"):
            print("You got burned")
        else:
            print("You win!")
    else:
        print("You drowned")
else:   
    print("You fell in a hole")
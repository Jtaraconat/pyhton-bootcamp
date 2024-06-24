#FOR LOOP
# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")


#AVERAGE HEIGHT CHALLENGE
# student_heights = [151, 145, 179]
# total_height = 0
# number_of_students = 0

# for height in student_heights:
#     total_height += height
# print(f"total height equals {total_height}")

# for student in student_heights:
#     number_of_students += 1
# print(f"number of students {number_of_students}")

# print(f"average height equals {int(total_height / number_of_students)}")


#HIGHEST SCORE CHALLENGE
# student_scores = [78,65,89,86,55,91,64,89]
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"the highest score of the class is: {highest_score}")



#LOOP AND RANGE FUNCTION
#for n in range(a,b):
    #do something
#excluding the b
#range from 1 to 10
# for n in range(1, 11):
#     print(n)

# #adding a step by 3
# for n in range(1,11,3):
#     print(n)

#add all number from 1 to 100 and get the sum
# total = 0
# for n in range(1,101):
#     total += n
# print(total)

#ADDING EVEN NUMBERS
# target = int(input("what's the target?"))
# total = 0

# if target > 0 and target <= 1000:
#     for n in range(0, target + 1):
#         if n % 2 == 0:
#             total += n
#     print(f"the total is {total}")
# else:
#     print("number must be between 0 and 1000")


#FIZZBUZZ GAME CHALLENGE
# for n in range(1,101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 5 == 0:
#         print("Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     else:
#         print(n)

#PASSWORD GENERATOR
# import random
# letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
# numbers = "0,1,2,3,4,5,6,7,8,9"
# symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# letters_list = letters.split(",")
# numbers_list = numbers.split(",")

# print("Welcome to the password generator")
# number_of_letters = int(input("How many letters would you like in your password?\n"))
# number_of_symbols = int(input("How many symbols would you like in your password?\n"))
# number_of_numbers = int(input("How many numbers would you like in your password?\n"))

# password_list = []
# password = ""


# for n in range(1, number_of_letters + 1):
#     password_list.append(random.choice(letters_list)) 

# for n in range(1, number_of_symbols + 1):
#     password_list.append(random.choice(symbols))

# for n in range(1, number_of_numbers + 1):
#     password_list.append(random.choice(numbers_list))

# random.shuffle(password_list)
# for char in password_list:
#     password += char

# print(f"your password is {password}")
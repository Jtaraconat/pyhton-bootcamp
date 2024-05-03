#Data types

#String 
#index in a String it's called subscripting
#print("hello"[0])
#print last char
#print("hello"[len("hello") - 1])

#Integer
#print(123 + 345)
#123_456_789 interpreted as 123456789 but easier to read

#Float
#3.14

#Boolean
#True or False capital first letter

#num_char = len(input("name?"))
#get type of variable
#print(type(num_char))

#type casting: from a data type to another
#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.")

#a = float(123)
#print(type(a))

#print(70 + float("100.5"))
#170.5

#add the 2 digits
#two_digit_number = 39
#two_digit_number_str = str(two_digit_number)
#digit_one = int(two_digit_number_str[0])
#digit_two = int(two_digit_number_str[1])
#total = digit_one + digit_two
#print(total)

#Math operations  3+5 3-5 3*5 3/5 
#division always return float
#power 2**2 2²
#order of priority PEMDAS parentheses, exponent, multiplication, division, addition, substraction
#between multiplication and division priority is the one on the left 

#BMI challenge
#height = float((input("What is your height in meters\n")))
#weight = int(input("Enter your weight in kilos\n"))
#bmi = int(weight / (height**2))
#print("Your bmi is " + str(bmi))

#round a float
#print(round( 8 / 3))

#round with 2 decimals 
#print(round( 8 / 3 , 2))

#integer with floor
#print(8 // 3)

#result and then result = result / 2
#result = 4 / 2
#result /= 2

#F string
#score = 0
#height = 1.9
#print("Your score is " + str(score))
#instead use f string
#print(f"your score is {score} and your are {height} meters" )

#age = input("What is your age?\n")
#total_weeks = 90 * 52
#age_in_weeks = int(age) * 52
#weeks_left = total_weeks - age_in_weeks
#print(f"You have {weeks_left} weeks left")

#Calculator challenge
#print("Welcome to the tip calculator")
#bill = float(input("what was the total bill? $"))
#tip_percentage = int(input("How much would you like to give? 10, 12, or 15?"))
#num_persons = int(input("How many people to split the bill?"))

#tip_amount = bill * (tip_percentage / 100)
#total_amount = tip_amount + bill
#bill_per_person = total_amount / num_persons
#format 2 decimals after the point
#split = "{:.2f}".format(bill_per_person)

#print(f"Each person should pay: ${split}")
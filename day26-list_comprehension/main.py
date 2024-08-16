#list comprehension-> create a new from a former list 
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#with list comprehension
#new_list = [new_item for item in list]
#better to type the list comprehension expression and replace the keywords
new_list_comprehension = [n+1 for n in numbers]

#Split the string in a list 
name = "Johan"
letters_list = [letter for letter in name]

#works with range
range_list = [n * 2 for n in range(1,5)]

#Conditional list comprehension 
#new_list [new_item for item in list if test]
names = ["alex", "beth","caroline","dave","eleanor","freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]

#check if a value in arr_1 is in arr_2
""" arr_1 = [1,2,3]
arr_2 = [3,4,5]

new_arr = [n for n in arr_1 if n in arr_2]
print(new_arr) """


#Dictionary comprehension
#new_dict = {new_key:new_value for item in list}
import random
#random score for a student in names
students_scores = {student:random.randint(0,100) for student in names}


#creating from an existing value in a dictionary
#new_dict = {new_key:new_value for(key,value) in dict.items()}
#create a new dict with student whom score are above 60
passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}

#Loop through dictionary
#for (key,value) in dictionary.items():
    #do something

import pandas
student_dict = {
    "student":["angela","james","lily"],
    "score":[56,76,98]
}
student_data_frame = pandas.DataFrame(student_dict)

#Loop through dataframe
""" for (key,value) in student_data_frame.items():
    print(value) """

#loop through rows
for (index, row) in student_data_frame.iterrows():
    #print(row) print both student and score
    #we can use the dot nnotation to get a specific key like print(row.student)
    if(row.student == "angela"):
        print(row.score)
#install module  
#py -m pip install pandas

import pandas as pd

#read a csv file
#data = pandas.read_csv(filepath_or_buffer="weather_data.csv")

#print the whole table
#print(data)

#print a specific column
#print(data["temp"])

#type of data variable
#return dataframe
#print(type(data))

#type of a column
#return a series
#print(type(data["temp"]))

#each series as a dictionnary
# data_dict = data.to_dict()
# print(data_dict)

#a series into a list
# temp_list = data["temp"].to_list
# print(temp_list)

#get average temp mean function
# avg_temp = data["temp"].mean()
# print(avg_temp)

#get data in column
# print(data["condition"])
# print(data.condition)

#get data in rows
# print(data[data.day == "Monday"])
#print a row based on a condition
# print(data[data.temp >= data.temp.mean()])

#filter a row by a condition and get a specific column
# monday = data[data.day == "Monday"]
# print(monday.condition)

#celsius to far
# temp_c = monday.temp
# temp_f = (temp_c * 9/5) + 32
# print(temp_f)

#Create a dataframe
# data_dict = {
#     "students": ["Amy", "James","Angela"],
#     "scores": [76,56,65]
# }

# data_students = pandas.DataFrame(data_dict)
# print(data_students)

#export to csv
# data_students.to_csv("new_data.csv")


#CHALLENGE 
#df = pandas.read_csv("squirrel_census.csv")
#get unique values of column
#print(df["Primary Fur Color"].unique())

# grey_squirrel_count = len(df[df["Primary Fur Color"] == "Gray"])
# black_squirrel_count = len(df[df["Primary Fur Color"] == "Black"])
# cinnamon_squirrel_count = len(df[df["Primary Fur Color"] == "Cinnamon"])


# squirrels_counts = {
#     "fur_color": ["grey", "black","cinnamon"],
#     "count": [grey_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
# }

# squirrels_counts_data = pandas.DataFrame(squirrels_counts)
# squirrels_counts_data.to_csv("squirrels_count_by_color.csv")





#GUESS THE STATES CHALLENGE
import turtle

screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()

guessed_states =[]


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 Guess the state', prompt="What's another state name?  \nType exit to get a csv with the missing states").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        #item return the item not the series with the index
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


#inheritance from a class Animal
#get all attributres and methods from animal class

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

# class Animal:
#     def __init__(self) -> None:
#         self.num_eyes = 2

#     def breathe(self):
#         print("inhale, exhale")

# class Fish(Animal):
#     def __init__(self) -> None:
#         super().__init__()

#     def swim(self):
#         print("moving in water")

# #Override breathe method, doing the same as in animal class and adding something to do
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater")

# nemo = Fish()
# nemo.breathe()
# nemo.swim()
# print(nemo.num_eyes)


from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
       
    #Detect collision with tail
    #slicing the list 
    # piano_keys = [a,b,c,d,e,f,g]
    # piano_keys[2:5] slice from position 2 to 5 => [c,d,e]
    # piano_keys[2:] slice all the way to the end from 2 => [c,d,e,f,g]
    # piano_keys[:5] slice all the way to 5 from 0 => [a,b,c,d,e]
    # piano_keys[2:5:2] slice from 2 to 5 with increment of 2 => [c,e]
    # piano_keys[::2] slice from 0 to the end with an increment of 2 => [a,c,e,g]
    # piano_keys[::-1] reverse the list => [g,f,e,d,c,b,a]
    # slicing work with tuple 

#check all segments from position 1 to the end, omitting the head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()







screen.exitonclick()
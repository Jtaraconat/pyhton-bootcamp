from turtle import Turtle, Screen
t = Turtle()
s = Screen()


#ETCH-A-SKETCH CHALLENGE
# def move_forward():
#     t.forward(10)

# def move_backward():
#     t.forward(-10)

# def counter_clockwise():
#     heading = t.heading()
#     angle = heading + 10
#     t.setheading(angle)

# def clockwise():
#     heading = t.heading()
#     angle = heading - 10
#     t.setheading(angle)

# def reset_drawing():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()

# s.listen()
# #eventlistner on keypress
# #function as input in function onkey()
# #onkey is a higher order function as it takes a function as input
# s.onkey(key="d", fun=move_forward)
# s.onkey(key="q", fun=move_backward)
# s.onkey(key="z", fun=counter_clockwise)
# s.onkey(key="s", fun=clockwise)
# s.onkey(key="c", fun=reset_drawing)



s.exitonclick()
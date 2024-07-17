from turtle import Turtle, Screen
import turtle as t
import random
#aliasing module import
#import turtle as t

t.colormode(255)
timmy = Turtle()
angle = [0,90,180,270]
#timmy.pensize(15)
timmy.speed("fastest")
# for _ in range(20):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides): 
#         timmy.forward(100)
#         timmy.right(angle)

# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)

#tuple is immutable, can't update the value
#tuple = (3, 2, 8)
#tuple[1]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# def draw_lines():
#     timmy.color((random_color()))
#     timmy.forward(20)
#     timmy.setheading(random.choice(angle))
    

# for steps in range(100):
#     draw_lines()



def spirograph(gap):
    for _ in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

spirograph(5)


screen = Screen()
screen.exitonclick()
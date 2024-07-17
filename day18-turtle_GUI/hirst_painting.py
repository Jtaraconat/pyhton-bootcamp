import colorgram
from turtle import Turtle, Screen

import random
# colors = colorgram.extract("img.jpg", 30)
# rgb_colors =[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [
(249, 228, 17), (213, 13, 9), (198, 12, 35), 
(231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)
]

t = Turtle()
s = Screen()

t.pensize(20)
steps = 50
s.colormode(255)
y_pos = 0
x_pos = 0


def draw_line(points):
    for _ in range(points):
        random_color = random.choice(color_list)
        t.pencolor(random_color)
        t.forward(1)
        t.pendown()
        t.forward(1)
        t.penup()
        t.forward(steps)

def next_line():
    t.penup()
    t.left(90)
    t.forward(steps)


for r in range (10):
    draw_line(10)
    y_pos += steps
    t.setpos(0,y_pos)
       

s.exitonclick()
# import colorgram
# colors = colorgram.extract('hirs.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.b
#     b = color.rgb.g
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
timmy = Turtle()
screen = Screen()
color_list = [(198, 32, 13), (248, 25, 236), (40, 188, 76), (244, 253, 247), (39, 69, 216), (238, 5, 227), (227, 49, 159), (29, 154, 40), (212, 15, 76), (17, 17, 153), (241, 161, 36), (195, 12, 16), (223, 120, 21), (68, 31, 10), (61, 8, 15), (223, 206, 141), (11, 62, 97), (219, 11, 159), (54, 229, 209), (19, 49, 21), (238, 216, 157), (79, 212, 74), (10, 238, 228), (73, 168, 212), (93, 198, 233), (65, 239, 231), (217, 51, 88)]
x = -250
y = -250

for k in range (10):
    timmy.penup()
    timmy.setposition(-250,y)
    y += 40
    x = -250
    for i in range (10):
        timmy.color()
        timmy.setposition(x,y)
        timmy.dot(20,random.choice(color_list))
        x+=40

screen.exitonclick()
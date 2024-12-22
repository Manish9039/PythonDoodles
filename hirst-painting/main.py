import turtle as t
import random

color_list = [(138, 78, 52), (49, 26, 23), (41, 78, 183), (196, 158, 118), (80, 234, 202), (66, 200, 226), (237, 169, 164), (240, 16, 16), (174, 178, 231), (224, 19, 119), (27, 40, 156), (81, 80, 213), (238, 227, 5), (248, 236, 31), (63, 233, 242), (225, 138, 205), (238, 156, 218), (19, 150, 23), (222, 78, 50), (11, 226, 238), (6, 245, 223), (10, 79, 111), (239, 41, 154), (18, 20, 44), (39, 213, 68), (195, 15, 11)]

tim = t.Turtle()
tim.shape("circle")

t.colormode(255)
tim.speed("fastest")

tim.setheading(225)
tim.penup()
tim.forward(255)
tim.setheading(0)

y = -180.31 + 50
def print_line():
    for _ in range(10):
        tim.color(color_list[random.randint(0, 25)])
        tim.stamp()
        tim.forward(50)

for _ in range(10):
    print_line()
    tim.teleport(-180.31, y)
    y += 50

tim.hideturtle()

screen = t.Screen()
screen.exitonclick()
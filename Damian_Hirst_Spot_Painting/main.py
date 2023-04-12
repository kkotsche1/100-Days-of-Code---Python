#
# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# color_list = []
# x = 0
# while x < len(colors):
#     color = colors[x]
#     rgb = color.rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     current_color = (red, green, blue)
#     color_list.append(current_color)
#     x += 1


from turtle import Turtle
from turtle import Screen
from random import randint

screen = Screen()
screen.colormode(255)
screen.setworldcoordinates(0,0,500,500)

tim = Turtle()
Turtle.colormode = 255
tim.penup()
tim.shape("turtle")
tim.color("darkorchid4")
tim.setpos(25, 25)
tim.speed(8)
tim.hideturtle()




color_list = [(198, 166, 109), (141, 77, 54), (73, 98, 123), (158, 148, 54), (213, 203, 144), (120, 39, 29), (137, 160, 179), (70, 108, 74), (144, 176, 139), (195, 91, 70), (69, 52, 46), (96, 81, 89), (60, 52, 56), (224, 177, 163), (102, 141, 131), (97, 130, 164), (156, 141, 159), (49, 60, 83), (73, 67, 50), (111, 38, 42), (47, 56, 72), (108, 136, 140), (182, 199, 183), (182, 190, 205), (168, 101, 106), (51, 76, 61)]
def spot_line(color_list):
    x = 0
    while x < 9:
        color = color_list[randint(0, 25)]
        tim.dot(20, color)
        tim.forward(50)
        x += 1
    tim.dot(20,color_list[randint(0, 25)])

def turn_tim_left():
    tim.left(90)
    tim.forward(50)
    tim.left(90)

def turn_tim_right():
    tim.right(90)
    tim.forward(50)
    tim.right(90)

z = 1

while z < 11:

    if z % 2 == 0:
        spot_line(color_list)
        turn_tim_right()
    else:
        spot_line(color_list)
        turn_tim_left()
    z += 1







screen.exitonclick()
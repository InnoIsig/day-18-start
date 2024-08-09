import  turtle as t
import random

tim = t.Turtle()

colors = ["medium sea green", "dark green", "indian red", "deep sky blue", "sea green", "dark slate gray","purple",
          "indian red"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for draw_shape_n in range(3, 8):
    tim.color(random.choice(colors))
    draw_shape(draw_shape_n)
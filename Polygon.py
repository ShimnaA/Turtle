# Draw a polygon using turtle

import turtle

window = turtle.getscreen()
t = turtle.Turtle()

num_of_sides = 9
angle = 360/num_of_sides


for i in range(num_of_sides):
    t.forward(50)
    t.right(angle)


# Draw a Spiral Square using turtle

import turtle

window = turtle.Screen()
window.bgcolor("yellow")

tt = turtle.Turtle()
tt.color("blue")

def draw_square(size):

    for i in range(4):
        tt.forward(size)
        tt.right(90)
        size = size - 5

size = 160
while size > 25:
    draw_square(size)
    size -= 20




# Draw spiral square inside out

import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

tt = turtle.Turtle()
tt.color("red")

def drawSquare(size):
    for i in range(4):
        tt.forward(size)
        tt.right(90)
        size = size + 5

size = 20
while size < 150:
    drawSquare(size)
    size += 20

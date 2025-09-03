import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
t.pensize(2)

colors = []
n = 36
for i in range(n):
    hue = i / n
    r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(hue, 1, 1)]
    colors.append((r, g, b))

for i in range(360):
    t.color(colors[i % n])
    t.forward(i * 2)
    t.right(144)   # star

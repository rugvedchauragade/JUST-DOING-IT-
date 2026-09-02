import turtle
import random

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor('black')
screen.colormode(255)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()

W = screen.window_width()
H = screen.window_height()

x = 0.0
y = 0.0

for i in range(60000):

    r = random.random()

    if r < 0.01:
        x, y = 0, 0.16 * y
        
    elif r < 0.86:
        x, y = (
            0.85 * x + 0.04 * y,
            -0.04 * x + 0.85 * y + 1.6
        )
        
    elif r < 0.93:
        x, y = (
            0.20 * x - 0.26 * y,
            0.23 * x + 0.22 * y + 1.6
        )
        
    else:
        x, y = (
            -0.15 * x + 0.28 * y,
            0.26 * x + 0.24 * y + 0.44
        )

    # fit to screen
    px = x * (H / 11)
    py = y * (H / 11) - H * 0.43

    # Orange + green
    ratio = max(0, min(1, y / 10))

    red = int(255 * (1 - ratio))
    green = int(70 + 185 * ratio)
    blue = int(15 + 25 * ratio)

    t.goto(px, py)
    t.dot(2, (red, green, blue))

    # visible drawing speed
    if i % 100 == 0:
        screen.update()

screen.update()
turtle.done()
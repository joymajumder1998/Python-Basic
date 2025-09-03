import turtle

# Setup screen
win = turtle.Screen()
win.title("Ping Pong Game 🏓")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Left paddle
left = turtle.Turtle()
left.speed(0)
left.shape("square")
left.color("white")
left.shapesize(stretch_wid=6, stretch_len=1)
left.penup()
left.goto(-350, 0)

# Right paddle
right = turtle.Turtle()
right.speed(0)
right.shape("square")
right.color("white")
right.shapesize(stretch_wid=6, stretch_len=1)
right.penup()
right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Score
score_left = 0
score_right = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal"))

# Functions for paddles
def left_up():
    y = left.ycor()
    if y < 250:
        left.sety(y + 20)

def left_down():
    y = left.ycor()
    if y > -240:
        left.sety(y - 20)

def right_up():
    y = right.ycor()
    if y < 250:
        right.sety(y + 20)

def right_down():
    y = right.ycor()
    if y > -240:
        right.sety(y - 20)

# Keyboard bindings
win.listen()
win.onkeypress(left_up, "w")
win.onkeypress(left_down, "s")
win.onkeypress(right_up, "Up")
win.onkeypress(right_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (top and bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball goes off right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        score_display.clear()
        score_display.write(f"Left: {score_left}  Right: {score_right}", align="center", font=("Courier", 24, "normal"))

    # Ball goes off left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        score_display.clear()
        score_display.write(f"Left: {score_left}  Right: {score_right}", align="center", font=("Courier", 24, "normal"))

    # Paddle collision (right)
    if (340 < ball.xcor() < 350) and (right.ycor() - 50 < ball.ycor() < right.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    # Paddle collision (left)
    if (-350 < ball.xcor() < -340) and (left.ycor() - 50 < ball.ycor() < left.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

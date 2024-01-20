import turtle
import time

# window settings
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(height=600,width=900)
wn.tracer(0)
wn.title("PARKOUR GAME")

# player
player = turtle.Turtle()
player.color("grey")
player.speed(0)
player.shape("square")
player.penup()
player.goto(-400,-250)
player.state = "ready"
player.dx = 0
player.dy = 0

# ground level

gl = turtle.Turtle()
gl.color("white")
gl.speed(0)
gl.shape("square")
gl.penup()
gl.goto(0,-280)
gl.shapesize(stretch_len=1000,stretch_wid=2)

# gravity
gravity = -0.0002

# functions
def jump():
    if player.state == "ready":
        player.dy = 0.2
        player.state = "jumping"

# keyboard binding
wn.onkeypress(jump, "space")



# main game loop

while True:
    wn.update()

    player.dy += gravity

    # jump
    y = player.ycor()
    y += player.dy
    player.sety(y)
    player.state = "jumping"

    if player.ycor() < -250:
        player.sety(-250)
        player.state = "ready"
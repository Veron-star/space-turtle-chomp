# setup screen
import turtle
turtle.setup(650,650)
# draw border
wn.bgcolor('darkseagreen')
# create player turtle
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
	mypen.forward(600)
	mypen.left(90)
mypen.hideturtle()
player = turtle.Turtle()
player.color('darkorange')
player.color('midnightblue')
player.shape('turtle')
player.penup()
player.speed(0)
# create food
food = turtle.Turtle()
food.color('navy')
food.shape('circle')
food.penup()
food.speed(0)
# set speed variable and keyboard binding
speed = 1
# define function
def turn_left():
	player.left(30)
def turn_right():
	player.right(30)
def increase_speed():
	global speed
	speed += 1
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
player.forward(speed)
# create player turtle
while True:
	player.forward(speed)
    # boundary layer checking X coordiante
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
    # boundary layer checking y coordiante
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)


	
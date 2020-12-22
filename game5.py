#Turtle Graphic Game - Space Turtle Chomp
import turtle
import math
import random
#set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('navy')
#draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
#create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup()
player.speed(0)
#create food
food = turtle.Turtle()
food.color('lightgreen')
food.shape('circle')
food.penup()
food.speed(0)
food.setposition(random.randint(-290, 290), random.randint(-290, 290))
#set speed variable
speed = 1 
#define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1
#set keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
while True:
    player.forward(speed)

    #boundary player checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    #boundary player checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

    #collision checking
    d = math.sqrt(math.pow(player.xcor() - food.xcor(), 2) + math.pow(player.ycor() - food.ycor(), 2))
    if d < 20:
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))
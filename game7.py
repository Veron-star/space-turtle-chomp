#Turtle Graphic Game - Space Turtle Chomp
import turtle
import math
import random
#set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('navy')
wn.bgpic('game-bg.gif')
wn.tracer(3)
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
max_foods = 10
foods = []
for count in range(max_foods):
    foods.append (turtle.Turtle())
    foods[count].color("lightgreen")
    foods[count].shape("circle")
    foods[count].penup()
    foods[count].speed(0)
    foods[count].shapesize(.5)
    foods[count].setposition(random.randint(-290, 290), random.randint(-290, 290))
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

    #move food around
    for food in foods:
        food.forward(3)

        #boundary food checking x coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(180)

        #boundary food checking y coordinate
        if food.ycor() > 290 or food.ycor() < -290:
            food.right(180)

        #collision checking
        d = math.sqrt(math.pow(player.xcor() - food.xcor(), 2) + math.pow(player.ycor() - food.ycor(), 2))
        if d < 20:
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
        
     

    
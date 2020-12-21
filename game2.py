#Turtle Graphic Game - Space Turtle Chomp
import turtle
#set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('navy')
#create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup()
player.speed(0)
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
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
#set speed variable
speed = 1
while True:
    player.forward(speed)
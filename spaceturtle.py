# Turtle Graphics Game - Space Turtle Chomp

import turtle

# set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('darkseagreen')

# create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.color('midnightblue')
player.shape('turtle')
player.penup()

#set speed variable
player.speed(0)
speed = 1
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
player.forward(speed)
while True:
	player.forward(speed)



	
import turtle
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('navy')
wn.bgcolor('lightcoral')
wn.bgcolor('darkseagreen')
player = turtle.Turtle()
player.color('darkorange')
player.color('midnightblue')
player.shape('turtle')
player.penup()
player.speed(0)
speed = 1
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
while True:
	player.forward(speed)



	
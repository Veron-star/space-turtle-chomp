Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.setup(650,650)
>>> wn = turtle.Screen()
>>> wn.bgcolor('navy')
>>> wn.bgcolor('lightcoral')
>>> wn.bgcolor('darkseagreen')
>>> player = turtle.Turtle()
>>> player.color('darkorange')
>>> player.color('midnightblue')
>>> player.shape('turtle')
>>> player.penup()
>>> speed = 1
>>> player.forward(speed)
>>> while True:
	player.forward(speed)
	
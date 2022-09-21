import turtle as t
import random

def move_up():
	t.setheading(90)
	t.forward(50)
	t.stamp()

def move_left():
	t.setheading(180)
	t.forward(50)
	t.stamp()

def move_down():
	t.setheading(270)
	t.forward(50)
	t.stamp()

def move_right():
	t.setheading(0)
	t.forward(50)
	t.stamp()	


def restart():
	t.reset()

t.shape("turtle")

t.onkey(move_up, 'w')
t.onkey(move_left, 'a')
t.onkey(move_down, 's')
t.onkey(move_right, 'd')
t.onkey(restart, 'Escape')
t.listen()

t.exitonclick()
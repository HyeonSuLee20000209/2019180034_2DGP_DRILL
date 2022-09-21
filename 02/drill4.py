import turtle as t

i = 6

t.left(90)

while i > 0:
    t.forward(500)
    t.penup()
    t.left(180)
    t.forward(500)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    i -= 1

i = 6
t.penup()
t.home()
t.pendown()

while i > 0:
    t.forward(500)
    t.left(180)
    t.penup()
    t.forward(500)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.pendown()
    i -= 1
    

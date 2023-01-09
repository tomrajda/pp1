from turtle import *

# circle
color('red', 'yellow')
r = 50
begin_fill()
circle(r)
end_fill()

penup()
goto(100, 100)
pendown()

# pentagon
l = 20
n = 5
for _ in range(n):
    forward(l)
    right(360 / n)

done()
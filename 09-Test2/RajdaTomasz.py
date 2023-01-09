import turtle
import math

def signature(a, x, y, color):
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.write("Tomasz Rajda\nZZISN1-1111", font=("Arial", a, "bold"))

def romb(a, x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.right(45)
    for _ in range(4):
        turtle.right(90)
        turtle.forward(a)
    turtle.end_fill()

def draw_circle(diameter, pen_color, fill_color, x, y):
    my_turtle = turtle.Turtle()
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.pencolor(pen_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(diameter / 2)
    my_turtle.end_fill()

def draw_triangle(side_length, pen_color, fill_color, x, y):
    my_turtle = turtle.Turtle()
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.pencolor(pen_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    for i in range(3):
        my_turtle.forward(side_length)
        my_turtle.left(120)
    my_turtle.end_fill()

def draw_star(side_length, pen_color, fill_color, x, y):
    my_turtle = turtle.Turtle()
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.speed(0)
    my_turtle.pencolor(pen_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    for i in range(5):
        my_turtle.forward(side_length)
        my_turtle.left(144)
    my_turtle.end_fill()

def draw_hexagon(side_length, pen_color, fill_color, x, y):
    my_turtle = turtle.Turtle()
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.pencolor(pen_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    for i in range(6):
        my_turtle.forward(side_length)
        my_turtle.left(60)
    my_turtle.end_fill()

def diamond(x,y, width, height, angle):
    turtle.up()
    turtle.color('red')
    turtle.goto(x,y-height/2)
    d = ((width/2)**2 + (height/2)**2)**0.5
    radius = d*0.5/math.sin(math.radians(angle/2))
    turtle.down()
    turtle.begin_fill()
    turtle.seth(turtle.towards(x-width/2,y)-angle/2)
    turtle.circle(radius, angle,20)
    turtle.seth(turtle.towards(x,y+height/2)-angle/2)
    turtle.circle(radius, angle,20)
    turtle.seth(turtle.towards(x+width/2,y)-angle/2)
    turtle.circle(radius, angle,20)
    turtle.seth(turtle.towards(x,y-height/2)-angle/2)
    turtle.circle(radius, angle,20)
    turtle.end_fill() 

diameters = [25, 50, 50, 25]
pen_colors = ['blue', 'orange', 'red', 'purple']
fill_colors = ['blue', 'orange', 'red', 'purple']

x = -200
y = 200
for i in range(4):
    draw_circle(diameters[i], pen_colors[i], fill_colors[i], x, y)
    x += 100

x = -200
y = 150
for i in range(4):
    draw_triangle(diameters[len(diameters)-i-1], pen_colors[len(diameters)-i-1], fill_colors[len(diameters)-i-1], x, y)
    x += 100

x = -200
y = 100
for i in range(4):
    diamond(x, y, diameters[i], diameters[i], 45)
    x += 100

x = -200
y = 0
for i in range(4):
    draw_hexagon(diameters[len(diameters)-i-1]/1.5, pen_colors[len(diameters)-i-1], pen_colors[len(diameters)-i-1], x, y)
    x += 100

x = -200
y = -50
for i in range(4):
    draw_star(diameters[i], pen_colors[i], fill_colors[i], x, y)
    x += 100

signature(20, 140, 140, "blue")

turtle.done()


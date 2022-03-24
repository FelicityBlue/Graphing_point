import turtle

# Ask for the position of the point

ws = turtle.Screen()

# Get input or both x-axis and y-axis
x_pos = float(turtle.textinput('Graphing', 'Enter x-axis (10 or under): '))
y_pos = float(turtle.textinput('Graphing', 'Enter y-axis (10 or under): '))

t = turtle.Turtle()
t.speed(10)

for i in range(0, 400, 20):
    t.pencolor('lightgrey')
    t.penup()
    t.setpos(-200 + i, -200)
    if i == 0:
        t.left(90)
    t.pendown()
    t.forward(400)
    t.backward(400)

for i in range(0, 400, 20):
    t.pencolor('lightgrey')
    t.penup()
    t.setpos(-200, -200 + i)
    if i == 0:
        t.right(90)
    t.pendown()
    t.forward(400)
    t.backward(400)

t.penup()
t.home()
t.pendown()

t.pencolor('black')
t.backward(200)
t.forward(400)
t.backward(200)

t.left(90)
t.forward(200)
t.backward(400)
t.penup()

t.setpos(5, 5)
t.pendown()
t.write(0)
t.penup()

t.setpos(190, 5)
t.pendown()
t.write('x')
t.penup()
t.setpos(5, 190)
t.pendown()
t.write('y')
t.penup()

t.setpos(0, -180)
t.pendown()


# go to 0,0
# go along x-axis
# go up or down depend on y input

t.penup()
t.home()

t.forward(20*x_pos)

t.left(90)
t.forward(20*y_pos)
t.pendown()
t.dot(10, 'red')
t.write("("+str(x_pos)+","+str(y_pos)+")")

turtle.Screen().exitonclick()
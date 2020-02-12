import turtle

a_turtle = turtle.Turtle()
a_turtle.penup()  # hide the pen for move
a_turtle.pensize(10)  # play with this it determines the outline width
a_turtle.color("red")
a_turtle.goto(100, 100)  # center of the circle is 100,100
a_turtle.pendown()  # get ready to draw
a_turtle.circle(50)  # radius of the circle is 20
#End of red ring

a_turtle.penup()  # hide the pen for move
a_turtle.pensize(10)  # play with this it determines the outline width
a_turtle.color("green")
a_turtle.goto(40, 50)  # center of the circle is 100,100
a_turtle.pendown()  # get ready to draw
a_turtle.circle(50)  # radius of the circle is 20
#End of green ring

a_turtle.penup()  # hide the pen for move
a_turtle.pensize(10)  # play with this it determines the outline width
a_turtle.color("black")
a_turtle.goto(-20, 100)  # center of the circle is 100,100
a_turtle.pendown()  # get ready to draw
a_turtle.circle(50)  # radius of the circle is 20
#End of black ring

a_turtle.penup()  # hide the pen for move
a_turtle.pensize(10)  # play with this it determines the outline width
a_turtle.color("yellow")
a_turtle.goto(-80, 50)  # center of the circle is 100,100
a_turtle.pendown()  # get ready to draw
a_turtle.circle(50)  # radius of the circle is 20
#End of yellow ring

a_turtle.penup()  # hide the pen for move
a_turtle.pensize(10)  # play with this it determines the outline width
a_turtle.color("blue")
a_turtle.goto(-140, 100)  # center of the circle is 100,100
a_turtle.pendown()  # get ready to draw
a_turtle.circle(50)  # radius of the circle is 20
turtle.done()
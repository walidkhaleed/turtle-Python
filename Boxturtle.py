#start the turtle
import turtle


f = turtle.Turtle()

f.speed(0)
f.color("white")
f.penup()
f.hideturtle()
f.goto(0, 250)
f.write("Welcome To Box-WAK", align="center", font=("Courier" , 24 , "normal"))


f = turtle.Turtle()
f.speed(0)
f.color("white")
f.penup()
f.hideturtle()
f.goto(0, -250)
f.write("Done By Walid A.K.", align="center", font=("Courier" , 24 , "italic"))


t = turtle.Turtle()

t.speed(0)
t.shape("turtle") #change the pen to tutle to enjoy

t.penup()
t.goto(-150 , -100)
t.pendown()

turtle.bgcolor("#141010")
x = 300

t.color('white')
for i in range(60): #to make our code more less in lines and time
    t.fd(x)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    x = x / 1.1

#make th main pen visible
t.penup()
t.forward(-800)
t.color("#6c8194")
t.pendown()

#extra code to enjoy
for i in range(3):
    t = turtle.Turtle()
    t.shape("turtle")
    t.penup()
    t.forward(-190)
    t.color('brown')
    t.pendown()

t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.forward(-190)
t.rt(90)
t.forward(40)
t.lt(90)
t.color('brown')
t.pendown()

t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.forward(-190)
t.lt(90)
t.forward(40)
t.rt(90)
t.color('brown')
t.pendown()


turtle.done() #end the turtle



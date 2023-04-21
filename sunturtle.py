class Sun():

    def su(self):
        import turtle

        turtle.speed(0)  # sets the speed of drawing to 0, which is the fastest
        turtle.pencolor('#ca27cb')  # sets the color of the pen/lines to white
        turtle.bgcolor("#0a0008")
        x = 0
        turtle.up()  # lifts up the pen, so no lines are drawn

        turtle.lt(90)
        turtle.fd(200)
        turtle.rt(85)
        turtle.fd(150)

        turtle.down()  # sets down the pen, so that turtle can draw
        while x < 50:  # while the value of x is lesser than 50,

            # continuously do this:
            turtle.fd(50)
            turtle.rt(61)
            turtle.fd(50)
            turtle.rt(61)
            turtle.fd(50)
            turtle.rt(61)
            turtle.fd(50)
            turtle.rt(61)
            turtle.fd(50)
            turtle.rt(61)
            turtle.fd(50)
            turtle.rt(61)

            turtle.rt(11.1111)
            x = x + 1


sun = Sun()
sun.su()

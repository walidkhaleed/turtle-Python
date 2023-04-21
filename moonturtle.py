class Moon():

    def mo(self):
        import turtle
        turtle.speed(0)
        turtle.speed(0)  # sets the speed of drawing to 0, which is the fastest
        turtle.pencolor('#b425ff')  # sets the color of the pen/lines to white

        x = 0
        turtle.up()  # lifts up the pen, so no lines are drawn

        turtle.lt(90)
        turtle.fd(-238)
        turtle.rt(90)
        turtle.fd(200)

        turtle.down()  # sets down the pen, so that turtle can draw
        while x < 50:  # while the value of x is lesser than 120,

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


moon = Moon()
moon.mo()

from sunturtle import Sun
from moonturtle import Moon

import turtle

WIDTH = 15
BRANCH_LENGTH = 120
ROTATION_LENGTH = 27
turtle.speed(0)

class Tree_Fractal(turtle.Turtle):
    turtle.speed(0)
    def __init__(self, level):
        super(Tree_Fractal, self).__init__()
        self.level = level
        self.hideturtle()
        self.speed('fastest')
        self.color("#8956fe")
        self.left(90)
        self.width(WIDTH)
        self.penup()
        self.back(BRANCH_LENGTH * 1.5)
        self.pendown()
        self.forward(BRANCH_LENGTH)
        self.draw_tree(BRANCH_LENGTH, level)

    def draw_tree(self, branch_length, level):
        width = self.width()
        self.width(width * 3. / 4.)
        branch_length *= 3. / 4.
        self.left(ROTATION_LENGTH)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.right(2 * ROTATION_LENGTH)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.left(ROTATION_LENGTH)

        self.width(width)
        turtle.speed(0)

if __name__ == '__main__':
    tree_level = 7# choose
    tree = Tree_Fractal(tree_level)

    turtle.done()




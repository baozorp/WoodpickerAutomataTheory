import turtle
import random


class Wood(turtle.Turtle):
    isWorm = None
    knocksForBoot = None

    def __init__(self, visible):
        super().__init__(visible=visible)
        self.newWorm()

    def newWorm(self):
        rand = bool(random.getrandbits(1))

        if rand:
            self.isWorm = True
            self.knocksForBoot = random.randint(3, 10)
        else:
            self.isWorm = False

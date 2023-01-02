import turtle
import random
from wood import Wood
from fox import Fox
from woodpicker import Woodpicker


class Forest:
    nest = turtle.Turtle(visible=False)
    height = 0
    width = 0
    soundOfNestlings = True
    woodpicker = None
    woods = None
    fox = None
    confines = None
    roar = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.confines()
        self.init_nest()
        self.init_woods()
        self.fox = Fox(visible=False, goalPosition=self.nest.position(), forest=self)
        self.woodpicker = Woodpicker(self)
        while True:
            self.woodpicker.stateManager()

    def confines(self):
        self.confines = turtle.Turtle(visible=False)
        self.confines.speed(0)
        self.confines.up()
        self.confines.pensize(5)
        self.confines.color('black')
        self.confines.goto(self.width, self.height)
        self.confines.down()
        self.confines.goto(self.width, -self.height)
        self.confines.goto(-self.width, -self.height)
        self.confines.goto(-self.width, self.height)
        self.confines.goto(self.width, self.height)
        self.confines.hideturtle()

    def init_nest(self):
        self.nest.shape("pictures/nest.gif")
        self.nest.up()
        self.nest.speed(0)
        self.nest.goto(random.randint(-self.width + 100, -100), random.randint(-self.height + 120, -100))
        self.nest.showturtle()

    def init_woods(self):
        counter = random.randint(6, 10)
        self.woods = []
        for _ in range(counter):
            wood = Wood(visible=False)
            self.woods.append(wood)
            wood.shape("pictures/wood.gif")
            wood.up()
            wood.speed(0)
            while wood.distance(self.nest) < 300:
                wood.goto(random.randint(-self.width + 60, self.width - 60),
                          random.randint(-self.height + 60, self.height - 60))
        for wood in self.woods:
            wood.showturtle()

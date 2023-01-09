import random
import turtle
from math import fabs
from time import sleep


class Woodpicker(turtle.Turtle):
    state = "Feed"
    turtleWoodpicker = turtle.Turtle(visible=False)
    propose = None
    startPosition = None
    isBoot = False

    def __init__(self, forest):
        self.forest = forest
        super().__init__(visible=False)
        self.speed(0)
        self.up()
        self.goto(forest.nest.position()[0], forest.nest.position()[1])
        self.speed(4)
        self.up()
        self.showturtle()

    def stateManager(self):
        print(self.state)

        if self.state == "Feed":
            if self.forest.soundOfNestlings and not self.forest.roar:
                self.feed()
                self.state = "Flight"
            else:
                self.state = "Defense"

        if self.state == "Flight":
            if self.distance(self.propose) > 40:
                self.flying()
                self.state = "Flight"

            elif self.distance(self.propose) < 40 \
                    and self.isBoot \
                    and not self.forest.roar:
                self.state = "Feed"
            elif self.distance(self.propose) < 40 \
                    and not self.isBoot \
                    and not self.forest.roar:
                self.state = "Search"
            elif self.distance(self.propose) < 40 and self.forest.roar:
                self.state = "Defense"

        if self.state == "Search":
            self.shape("pictures/woodpicker3.gif")
            sleep(1)
            if self.propose.isWorm:
                self.state = "Booty"
            else:
                self.search()
                self.state = "Flight"

        if self.state == "Booty":
            if self.propose.knocksForBoot > 0 and not self.forest.roar:
                self.booty()
                self.state = "Booty"
            else:
                self.propose = self.forest.nest
                self.startPosition = self.position()
                self.state = "Flight"

        if self.state == "Defense":
            if self.forest.roar:
                self.state = "Defense"
                self.defense()
            elif self.isBoot:
                self.state = "Feed"
            else:
                self.state = "Flight"

    def defense(self):
        if self.forest.fox.knoxForRunning == 0:
            self.forest.fox.hide()
            self.forest.roar = False
            for wood in self.forest.woods:
                wood.newWorm()
            self.propose = self.forest.woods[random.randint(0, len(self.forest.woods) - 1)]
            self.startPosition = self.position()
        else:
            self.goto(self.forest.fox.position()[0] + random.randint(-30, 30),
                      self.forest.fox.position()[1] + random.randint(-30, 30))
            self.forest.fox.knoxForRunning -= 1

    def feed(self):
        self.shape("pictures/woodpicker2.gif")
        self.isBoot = False
        for wood in self.forest.woods:
            wood.newWorm()
        self.propose = self.forest.woods[random.randint(0, len(self.forest.woods) - 1)]
        self.startPosition = self.position()
        rand = random.randint(0, 100)
        if rand > 95 and not self.forest.roar:
            self.forest.fox.attack()
            self.forest.roar = True
            self.propose = self.forest.fox
            self.startPosition = self.position()

    def booty(self):
        self.shape("pictures/woodpicker4.gif")
        sleep(0.5)
        self.propose.knocksForBoot -= 1
        if self.propose.knocksForBoot == 0:
            self.isBoot = True
            self.shape("pictures/woodpicker1.gif")

    def search(self):
        for wood in self.forest.woods:
            wood.newWorm()
        nextPropose = self.forest.woods[random.randint(0, len(self.forest.woods) - 1)]
        while self.propose == nextPropose:
            nextPropose = self.forest.woods[random.randint(0, len(self.forest.woods) - 1)]
        self.shape("pictures/woodpicker2.gif")
        self.propose = nextPropose
        self.startPosition = self.position()

    def flying(self):
        rand = random.randint(0, 100)
        if rand > 98 and not self.forest.roar:
            self.forest.fox.attack()
            self.forest.roar = True
            self.propose = self.forest.fox
            self.startPosition = self.position()

        if self.startPosition[0] > self.propose.position()[0]:
            x = self.position()[0] - fabs(
                self.propose.position()[0] - self.startPosition[0]) / random.randint(15, 20)
        else:
            x = self.position()[0] + fabs(
                self.propose.position()[0] - self.startPosition[0]) / random.randint(15, 20)
        if self.startPosition[1] > self.propose.position()[1]:
            y = self.position()[1] - fabs(
                self.propose.position()[1] - self.startPosition[1]) / random.randint(15, 20)
        else:
            y = self.position()[1] + fabs(
                self.propose.position()[1] - self.startPosition[1]) / random.randint(15, 20)
        self.goto(x, y)

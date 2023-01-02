import random
import turtle


class Fox(turtle.Turtle):

    knoxForRunning = None
    goalPosition = None

    def __init__(self, visible, goalPosition, forest):
        super().__init__(visible=visible)
        self.widthh = None
        self.heightt = None
        self.goalPosition = goalPosition
        self.forest = forest
        self.up()
        self.speed(0)
        self.goto(self.forest.width + 200, self.forest.height + 200)
        self.hideturtle()
        self.hide()
        self.shape("pictures/fox.gif")

    def hide(self):
        rand = random.randint(1, 4)
        match rand:
            case 1:
                self.widthh = -self.forest.width - 200
                self.heightt = -self.forest.height - 200
            case 2:
                self.widthh = -self.forest.width - 200
                self.heightt = self.forest.height + 200
            case 3:
                self.widthh = self.forest.width + 200
                self.heightt = -self.forest.height - 200
            case 4:
                self.widthh = self.forest.width + 200
                self.heightt = self.forest.height + 200
        self.speed(5)
        self.knoxForRunning = random.randint(5, 10)
        self.goto(self.widthh, self.heightt )
        self.hideturtle()

    def attack(self):
        self.forest.roar = True
        self.knoxForRunning = random.randint(3, 5)
        self.hideturtle()
        self.speed(0)
        self.goto(self.widthh, self.heightt)
        self.showturtle()
        self.speed(5)
        self.goto(self.goalPosition[0], self.goalPosition[1])

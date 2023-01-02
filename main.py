import os
import turtle
from forest import Forest

turtle.Screen().setup(800, 800)
turtle.screensize(360, 360)
height = turtle.screensize()[0]
width = turtle.screensize()[1]


if __name__ == '__main__':
    for picture in os.listdir("pictures"):
        if picture.endswith(".gif"):
            print("pictures/" + picture)
            turtle.register_shape("pictures/" + picture)
    window = turtle.Screen()
    window.bgcolor('green')
    window.title("Woodpicker")
    forest = Forest(height, width)


from visual import *
import random

def spinBox():
    myBox = box(color = (1.0, 0.0, 0.0))
    while True:
        # Slow down the animation to 60 frames per second.
        # Change the value to see the effect!
        rate(60)
        myBox.rotate(angle=pi/100)

def spinBoxes():
    boxList = []
    for boxNumber in range(10):
        x = random.randint(-5, 5) # integer between -5,5
        y = random.randint(-5, 5)
        z = random.randint(-5, 5)
        red = random.random()     # real number between 0 & 1
        green = random.random()
        blue = random.random()
        newBox = box(pos = vector(x, y, z),
                     color = (red, green, blue) )
        boxList.append(newBox)
    while True:
        for myBox in boxList:
            rate(100)
            myBox.rotate(angle=(pi/50)*random.random())

print vector(1,2,3)
spinBoxes()

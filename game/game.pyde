import random

class enemy:
    def __init__(self, x, y, endx, enemy):
        self.x = x
        self.y = y
        self.endx = endx
        self.enemy = enemy

class hole:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    def drawhole(self):
        stroke(255)
        rect(self.x1, height - 100, self.x2, height)

def setup():
    global death, jump, still, run1, run2, marioy, holelist
    size(1366, 768)
    death = loadImage("death.png")
    jump = loadImage("jump.png")
    still = loadImage("mario still.png")
    run1 = loadImage("running1.png")
    run2 = loadImage("running2.png")
    marioy = height - 149
    holelist = []
    hole1 = hole(0, 100)
    hole2 = hole(250, 350)
    holelist.append(hole1)
    holelist.append(hole2)
    
def draw():
    background(0)
    rect(0, 0, width, height - 100)
    for i in holelist:
        i.drawhole()
    image(still, width / 2, marioy, 50, 50)
    

def keyPressed():
    if key == "w":
        while marioy > height - 259:
            marioy -= 10
            image(jump, width / 2, marioy, 50, 50)
        while marioy < height -159:
            marioy += 10
    if key == "d":
        for i in holelist:
            i.x1 -= 10
            #i.x2 -= 1
    if key == "a":
        for i in holelist:
            i.x1 += 10
            #i.x2 += 1

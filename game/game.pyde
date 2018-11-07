import random

class enemy:
    def __init__(self, x, y, endx, enemy):
        self.x = x
        self.y = y
        self.endx = endx
        self.enemy = enemy

class ground:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x1 = x2
    def drawline:
        stroke(255)
        line(x1, height - 100, x2 , height - 100)

def setup():
    global death, jump, still, run1, run2
    size(displayWidth, displayHeight)
    death = loadImage("death.png")
    jump = loadImage("jump.png")
    still = loadImage("mario still.png")
    run1 = loadImage("running1.png")
    run2 = loadImage("running2.png")
    marioy = height - 149
    platformlist = []
    for i in range(100):
        platform = ground(random.randint(
    
def draw():
    background(0)
    rect(0, 0, height - 99, width)
    if not keyPressed:
        image(still, width / 2, marioy, 50, 50)
    

def keyPressed():
    if key == "w":
        while marioy > height - 259:
            marioy -= 10
            image(jump, width / 2, marioy, 50, 50)
        while marioy < height -159:
            marioy += 10
    if key == "d":
        for i in platformlist:
            i.x1 += 10
            i.x2 += 10
            

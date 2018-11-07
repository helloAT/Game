def setup():
    global death, jump, still, run1, run2
    size(displayWidth, displayHeight)
    death = loadImage("death.png")
    jump = loadImage("jump.png")
    still = loadImage("mario still.png")
    run1 = loadImage("running1.png")
    run2 = loadImage("running2.png")
    platform_list = [

def draw():
    

def keyPressed():
    if key == "w":
        

class enemy:
    def __init__(self, x, y, endx, enemy):
        self.x = x
        self.y = y
        self.endx = endx
        self.enemy = enemy

class piranha:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def run():
        

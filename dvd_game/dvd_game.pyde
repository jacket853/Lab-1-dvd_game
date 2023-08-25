RAD = 30

XSPEED = 4
YSPEED = 3

xpos = 0.0
ypos = 0.0

xdir = -1
ydir = -1

def setup():
    global RAD, XSPEED, YSPEED, xpos, ypos, xdir, ydir
    size(600, 500)
    frameRate(60)
    ellipseMode(RADIUS) # default mode is ellipseMode(CENTER)
    
    xpos = width/2
    ypos = height/2
    

def draw():
    global RAD, XSPEED, YSPEED, xpos, ypos, xdir, ydir
    xpos = xpos+(XSPEED*xdir)
    ypos = ypos+(YSPEED*ydir)
    
    if (xpos > width-RAD) or (xpos < RAD):
        xdir *= -1
    if (ypos > height-RAD) or (ypos < RAD):
        ydir *= -1
        
    fill(204, 102, 0)
    ellipse(xpos, ypos, RAD, RAD)

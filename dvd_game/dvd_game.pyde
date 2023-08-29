

XSIZE = 600
YSIZE = 500
FRAMERATE = 30

def setup():
    size(XSIZE, YSIZE)
    noStroke()
    frameRate(FRAMERATE)
    ellipseMode(RADIUS)
    xside = Edge(XSIZE)
    yside = Edge(YSIZE)

def draw():
    background(0,0,0)
    disk = Dvd(30, xside.x/2, yside.y/2, 4, 3, -1, -1)
    disk.checkEdge()
    disk.drawDisk()

class Edge(object):
    # the edge of the screen, used to define rebound, starting point, etc.
    def __init__(self, x=None, y=None):
        # x and y are optional, if one is not put in, then the other is None/default value
        if x is None and y is None:
            raise ValueError("Can't create Edge instance with no coordinate given.  Provide either an x or a y coordinate.")
        if x is not None and y is not None:
            raise ValueError("Can't create Edge instance with both coordinate given.  Provide either an x or a y coordinate.")
        
        self.x = x
        self.y = y

class Dvd(object):
    def __init__(self, rad, xpos, ypos, xspeed, yspeed, xdir, ydir):
        self.rad = rad
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xdir = xdir
        self.ydir = ydir
    
    def drawDisk(self):
        # update position based on checkEdge() method
        self.xpos = self.xpos+(self.xspeed*self.xdir)
        self.ypos = self.ypos+(self.yspeed*self.ydir)
        
        fill(204, 102, 0)
        ellipse(self.xpos, self.ypos, self.rad)
    
    def checkEdge(self):
        if (self.xpos > XSIZE-self.rad) or (self.xpos < selfrad):
            self.xdir *= -1
        if (self.ypos > YSIZE-self.rad) or (self.ypos < self.rad):
            self.ydir *= -1

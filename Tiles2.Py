import random
import os
import shlex
import random
import math
#Make the file
os.remove("Tiles.eps")
f = open("Tiles.eps", "x")
f.write("""
    %!PS-Adobe-3.0 EPSF-3.0 \n
    %%BoundingBox: 0 0 60 70 \n

    0.7 setgray \n

    1 setlinejoin \n
    1 setlinecap \n

    /r 2 def \n
    newpath \n
    """)
#All boxes radius 100
#Draw the first box

def drawBox(x,y):
    f.write("""
    %Box
    newpath \n""")
    f.write(str(x) + " " + str(y) + " moveto\n")
    f.write("""
    0 100 rlineto\n
    100 0 rlineto\n
    0 -100 rlineto\n
    -100 0 rlineto\n
    stroke\n
    closepath\n
    """)

def roundUp(x):
    return int(math.ceil(x / 100.0)) * 100

def roundDown(x):
    return int(math.floor(x / 100.0)) * 100

def drawFull(x):
    #X = number of boxes to pass through
    points = []
    rlines = []
    points.append([random.randrange(0,600,100),random.randrange(0,700,100)])
    f.write("newpath\n" + str(points[0][0]) + " " + str(points[0][1]) + " " + " moveto \n")

    for x in range(1, 2):
        previousx = points[0][0]
        previousy = points[0][1]
        rlines.append([previousx, random.randrange(0,100,10)])
        f.write(str(100) + " " + str(rlines[0][1]) + " rlineto \n")


    f.write("stroke\n closepath\n")
    print(points)

def drawLine(x):
    dir = [-50, 50, -25, 25]

    f.write("newpath\n" + "350 400 moveto \n")
    for i in range(0,x):
        one = random.choice(dir)
        two = random.choice(dir)
        f.write(str(one) + " " + str(two) + " rlineto \n")
    f.write("stroke\n closepath\n")

def drawCurve(x):
    dir = [-50, 50, -25, 25]

    f.write("newpath\n" + "350 300 moveto \n")
    for i in range(0,x):
        one = random.choice(dir)
        two = random.choice(dir)
        f.write(str(one) + " " + str(two) + " curveto \n")
    f.write("stroke\n closepath\n")

def drawBoxLine(x, y):

    f.write("newpath\n" + str(x) + " " + str(y) + " moveto\n")

    f.write(str(100 - x) + " " + str(100-y)  + " rlineto\n")

    f.write("stroke \n closepath \n")

def drawBox2(x,y):
    f.write("""
    %Box
    newpath \n""")
    f.write(str(x) + " " + str(y) + " moveto\n")
    f.write("""
    0 25 rlineto\n
    25 0 rlineto\n
    0 -25 rlineto\n
    -25 0 rlineto\n
    stroke\n
    closepath\n
    """)



for x in range(0,600, 25):

    for y in range(0,700, 25):
        drawBox2(x,y)

drawLine(500)
drawLine(500)
drawLine(500)
drawLine(500)

f.write("""closepath \n
        gsave \n
        showpage\n
        %EOF% \n""")

os.system("open " + shlex.quote("Tiles.eps"))

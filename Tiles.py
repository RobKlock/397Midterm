import random
import os
import shlex
import random
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
def drawFull(x):
    #X = number of boxes to pass through
    points = []
    for i in range(0, x):
        choice = random.randint(0,1)
        if choice == 0:
            xcoor = random.randrange(0,625,100)
                #TODO: fix coordinates so theyre restricted to length 100. maybe use rlineto?

            temp = [xcoor, random.randrange(0, 710,10)]
        if choice == 1:
            temp = [random.randrange(0,610,10), random.randrange(0, 725,100)]
        # if choice == 0:
        #     temp = [random.randrange(0,625,100), random.randrange(0, 710,10)]
        # if choice == 1:
        #     temp = [random.randrange(0,610,10), random.randrange(0, 725,100)]

        points.append(temp)
    f.write("newpath\n" + str(points[0][0]) + " " + str(points[0][1]) + " " + " moveto \n")
    for x in range(1, x-1):
        f.write(str(points[x][0]) + " " + str(points[x][1]) + " lineto \n")

    f.write("stroke\n closepath\n")
    print(points)
#Draw the lines of the box

def drawBoxLine(x, y):
    #X and Y are the lower left point of the square we deal with
        #possible values are all permutations of x = 0, y = 0, and then x and y ranging between 0 and 100


    #Have to keep track of where the previous line was drawn, then go to that line
    f.write("newpath\n" + str(x) + " " + str(y) + " moveto\n")

    # randx = random.randint(x1, x1 + 100)
    # randy = random.randint(y1, y1 + 100)
    # randc = random.randint(100,105)

    f.write(str(100 - x) + " " + str(100-y)  + " rlineto\n")
    # f.write(str(randx + 100) + " 100 " + str(randy + 100) + " \n")
    # #f.write(str(randx  + 50) + " 100 " + str(randy + 50) + " \n")
    # #f.write(str(randx) + " 0 " + " curveto\n")
    #
    #f.write(str(y + 50)+ " "  + str(50) + " rlineto\n stroke\n closepath\n")
    f.write("stroke \n closepath \n")

    #Just choose a bunch of points on a 700 by 600 grid, separated by
    #a vertical distance of 100, and draw a line connecting them


for x in range(0,600, 100):
    #drawBoxLine(x,x,x+100, x+100, x)
    for y in range(0,700, 100):
        drawBox(x,y)

#for x in range(0,10):
#    ranx = random.randint(0,600)
#    rany = random.randint(0,700)
#    drawBoxLine(ranx, rany)

#drawFull(10)

drawFull(5)





# for x in range(0,500, 100):
#     #drawBoxLine(x,x,x+100, x+100, x)
#     for y in range(0,600, 100):
#         drawBoxLine(x,y)


f.write("""closepath \n
        gsave \n
        showpage\n
        %EOF% \n""")

os.system("open " + shlex.quote("Tiles.eps"))

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
    for i in range(0, x):
        print(points)
        print(i)
        choice = random.randint(0,1)
        #Choice = 0, fix the points onto an X grid line
        #choice = 1, fix the pints onto a Y grid line

        if (i == 0):
            #Initialize first point
            if choice == 0:
                #x is fixed onto a grid line
                temp = [random.randrange(0,601,100), random.randrange(0, 710,10)]

            if choice == 1:
                #y is fixed onto a grid line
                temp = [random.randrange(0,609,10), random.randrange(0, 725,100)]

            points.append(temp)

        elif (i>0):

            if choice == 0:
                print(str(0) + " " + str(0))
                #fix on x line
                previousx = points[i-1][0]
                previousy = points[i-1][1]
                #print("prevx " + str(previousx))
                #print("prevy " + str(previousy))

                if (previousy % 100 == 0): #If the x coordiate is stable
                    #Choose a x within a range of 100
                    if (previousx == 0):
                        new_x = random.randrange(0,100,10)
                    elif (previousy == 0):
                        new_y = random.randrange(0,101,100)
                    else:
                        new_x = random.randrange(roundDown(previousx), roundUp(previousx), 10)
                        new_y = random.randrange(previousy - 100, previousy + 100, 100)

                    temp = [new_x, new_y]


                else:
                    print(str(0) + " " + str(1))
                    new_x = random.randrange(previousx - 100, previousx + 100, 100)
                    new_y = random.randrange(roundDown(previousy), roundUp(previousy), 10)

                    temp = [new_x, new_y]



            if choice == 1:

                previousx = points[i-1][0]
                previousy = points[i-1][1]
                print("prevx " + str(previousx))
                print("prevy " + str(previousy))

                if (previousy % 100 == 0):
                    print(str(1) + " " + str(0))
                    if (previousy == 0):
                        new_y = random.randrange(previousy, 101, 100)
                    elif (previousx == 0):
                        new_x = random.randrange(previousx, 101, 10)
                    else:
                        print("RD prevx: " + str(roundDown(previousx)))
                        print("RU prevx: " + str(roundUp(previousx)))
                        new_y = random.randrange(previousy - 100, previousy + 100, 100)
                        new_x = random.randrange(roundDown(previousx), roundUp(previousx), 10)

                    temp = [new_x, new_y]


                else:
                    print(str(1) + " " + str(1))
                    new_y = random.randrange(roundDown(previousy), roundUp(previousy), 100)
                    new_x = random.randrange(previousx - 100, previousy + 10, 100)

                    temp = [new_x, new_y]


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

drawFull(10)
#print (roundUp(455))
#print (roundDown(444))




# for x in range(0,500, 100):
#     #drawBoxLine(x,x,x+100, x+100, x)
#     for y in range(0,600, 100):
#         drawBoxLine(x,y)


f.write("""closepath \n
        gsave \n
        showpage\n
        %EOF% \n""")

os.system("open " + shlex.quote("Tiles.eps"))

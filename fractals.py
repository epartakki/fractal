## ------------------------------------------------------
##        Utilizing Fractals and Turtle Graphics
## ------------------------------------------------------
import turtle
from time import sleep

maxFractalSize = 5          # Num Factral
val_x = -150                # Initial X coordinate
val_y = 0                   # Initial Y coordinate
size = 300                  # Size of Fractal
myDelay = 2                 # Seconds Between Fractals
myColor = ["orange", "blue", "red", "green", "purple", "brown"]

def drawFractal(t, order, size):
    if order == 0:
       t.forward(size) # The base case is just a straight line
    else:
        t.left(90) #rotate 90 degrees to the left
        drawFractal(t, order-1, size/2)    # draw the first line (1/2 as big)
        t.right(135)                  # rotate 135deg to the right
        drawFractal(t, order-1, size * .707)    # draw second line (1/2*sqrt(2) because it's the hypotenuse
        t.left(45)# rotate 45deg to the left
        t.penup()    # pick pen up so no line is drawn
        t.forward(size/2) #go forward
        t.pendown() #put pen down so lines can be drawn
        t.left(180) #flip turtle to go opposite direction
        drawFractal(t, order-1, size/2) #draw the third line backwards/right to left (turtle goes back towards the dragon)
        t.penup() # pick pen up so no line is drawn
        t.right(180) #flip turtle to go opposite direction (away from dragon)
        t.forward(size/2) #move turtle back to the end of the third line (away from rest of dragon)
        t.pendown() #put pen down so lines can be drawn





def main(maxFractalSize, size, x, y, myColor, myDelay):   
    iTurtle = turtle.Turtle()
    window = turtle.Screen()
    print(iTurtle.pos())
    for i in range(maxFractalSize):
        iTurtle.reset()
        iTurtle.hideturtle()
        iTurtle.color(myColor[i])
        iTurtle.penup()
        iTurtle.setposition(x,y)
        iTurtle.pendown()
        drawFractal(iTurtle, i, size)
        sleep(myDelay)
if __name__ == "__main__":
    main(maxFractalSize + 1, size, val_x, val_y, myColor, myDelay)

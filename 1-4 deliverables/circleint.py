# circleint.py
# Created on 1/3/18 by Jenna Folsom
# A program that computes the intersection of a circle with a horizontal line and displays the information textually and graphically

from graphics import *
import math

def main():

    # This is an introduction
    print("This program computes the intersection of a circle with a horizontal line and displays the information textually and graphically.")

    # This is an input
    r = eval(input("What is the radius of the circle? "))
    y = eval(input("What is the y-intercept of the line? "))

    # This is an output
    win = GraphWin()
    win.setCoords(-10.0, -10.0, 10.0, 10.0)
    circle = Circle(Point(0.0,0.0), r)
    circle.draw(win)

    line = Line(Point(-10, y), Point(10, y))
    line.draw(win)
    
    # This is also an output
    x = abs(math.sqrt(r**2 - y**2))
    x2 = x * -1
    print("The x values for the intersections are", x , "and", x2)
    # click mouse anywhere to close
    win.getMouse()
    win.close()

main()    

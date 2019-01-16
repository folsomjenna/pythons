# rect.py
# Created on 1/4/18 by Jenna Folsom
# This program displays information about a rectangle drawn by the user. 

from graphics import *
import math

def main():
    #This is an intro.
    print("This program displays information about a rectangle drawn by the user.")
    win = GraphWin()
    clickPoint = win.getMouse()
    p1 = clickPoint.getX()
    p2 = clickPoint.getY()
    aRectangle = Rectangle(Point(1, 3), Point(4, 7))
    
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on two points")
    message.draw(win)
    
    #Draws 4 vertices of rectangle
    p1 = win.getMouse()
    p2 = win.getMouse()
    
    p4 = Point((p2.getY()), (p1.getX()))
    p7 = Point((p1.getX()), (p2.getY()))
 
    # Used Polygon object to draw the rectangle
    shape = Rectangle(p1, p2)
    shape.setFill("cyan")
    shape.setOutline("blue")
    shape.draw(win)
    
    # Formulas for Height and Width
    width = abs(p2.getX() - p1.getX()) 
    length = abs(p2.getY() - p1.getY())
    
    # Formulas for a rectangle
    area =  length * width 
    perimeter = 2 * (length + width)

    print("The perimeter of the rectangle is", perimeter)
    print("The area of the rectangle is", area)
main()

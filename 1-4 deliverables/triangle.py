# triangle.py
# Created by Jenna Folsom on 1/15/19
# This program displays information about a triangle drawn by a user.

from graphics import *
import math

def main():
    # This is an intro.
    print("This program displays the area and perimeter of a triangle drawn by a user.")
    
    win  = GraphWin()
    clickPoint = win.getMouse()
    p1 = clickPoint.getX()
    p2 = clickPoint.getY()
    p3 = clickPoint.getX()
    aTriangle = Polygon(Point(1, 3), Point(4, 7), Point(-1, -3))

    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points.")
    message.draw(win)

    # Draws 3 vertices of a triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    # Used polygon object to draw the rectangle
    shape = Polygon(p1, p2, p3)
    shape.setFill("purple")
    shape.setOutline("black")
    shape.draw(win)
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    
    # Formulas for height, width, and side
    s = abs(p1.getX() - p1.getY()) + abs(p2.getX() - p2.getY()) + abs(p3.getX() - p3.getY()) / 2
    width = abs(p2.getX() - p1.getX())
    length = math.sqrt(dx ** 2 + dy ** 2)

    # Formulas for a triangle
    perimeter = abs(2 * (length + width))
    area = math.sqrt(s * (s - (p1.getY() - p1.getX())) * (s - (p2.getY() - p2.getX())) * (s - (p3.getY() - p3.getX())))

    # Displays info to reader
    print("The area of your triangle is: ", area, "cubic units.")
    print("The perimeter of your triangle is: ", perimeter, "units.")
    
main()

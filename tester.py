# 1.py
# Created on 12/12/18 by Jenna Folsom
# A program that prints squares the user clicks

from graphics import *

def main():
     win = GraphWin()
     shape = Rectangle(Point(50,50), Point(20,20))
     shape.setOutline("red")
     shape.setFill("red")
     shape.draw(win)
     for i in range(10):
          p = win.getMouse()
          c = shape.getCenter()
          dx = p.getX() - c.getX()
          dy = p.getY() - c.getY()
          shape = shape.clone()
          shape.move(dx,dy)
          shape.draw(win)

     s = Text(Point(100,100), "Click again to quit.")
     s.draw(win)
     win.getMouse()
     win.close()

main()

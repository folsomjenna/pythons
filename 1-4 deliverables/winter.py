# winter.py
# Created on 12/13/18 by Jenna Folsom
# A program that draws a winter scene with a tree and a snowman

from graphics import *
 
win = GraphWin('Snowman', 400, 400)
win.setBackground('lightskyblue')
 
def shapes(x,y,dx,dy):
    for i in range (3):
        shape = Oval(Point (x,y), Point(dx,dy))
        shape.setFill('white')
        shape.setOutline('white')
        shape.draw(win)
        tri = Polygon(Point(270,y-50),Point(x+170,y+10),Point(dx+200,y+10))
        tri.setFill('green')
        tri.setOutline('green')
        tri.draw(win)
        x = x-10
        y = y+50
        dx = dx+10
        dy = dy+55
        tri = Polygon(Point(x+150,y+50),Point(x+125,y-25),Point(x+175,y-25))
    return shapes
 
def main():
 
    land = Oval(Point(-150,280),Point(500,500))
    land.setFill('gray92')
    land.setOutline('gray')
    land.draw(win)
    
    trunk = Line(Point(270,200), Point(270,350))
    trunk.setOutline('chocolate')
    trunk.setWidth(10)
    trunk.draw(win)
    
    shapes(50,150,120,210)
    eye1 = Circle(Point(70,175),5)
    eye1.setFill('black')
    eye1.draw(win)
    eye2 = eye1.clone()
    eye2.move(30,0)
    eye2.draw(win)
    
    mouth = Oval(Point(70,190),Point(100,195))
    mouth.setFill('red')
    mouth.draw(win)
    
    nose = Polygon(Point(85,175), Point(80,185), Point(90,185))
    nose.setFill('orange')
    nose.draw(win)
    
    rect = Rectangle(Point(20,312), Point(150,350))
    rect.setFill('gray92')
    rect.setOutline('gray92')
    rect.draw(win)
 
    win.getMouse()
    win.close()
 
main()

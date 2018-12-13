# dice.py
# Created on 12/13/18 by Jenna Folsom
# A program that draws 5 dice

from graphics import *
import string
 
win = GraphWin('Dice', 400, 400)
win.setBackground('gray')
win.setCoords(0,0,20,20)
 
# Draws 5 dice on the screen
def main():
     
    die = Polygon(Point(2,17),Point(4,16), Point(6,17), Point(6,15), Point(4,14),
        Point(4,16),Point(4,14),Point(2,15), Point(2,17),
        Point(4,18),Point(6,17),Point(4,16),Point(2,17))
    die.setFill('white')
    die.setOutline('black')
    die.setWidth('2')
    die.draw(win)
    dx = 0
    dy = 0
    for i in range(1,5):
        dx = dx + 3
        dy = dy - 3
        dice = die.clone()
        dice.draw(win)
        dice.move(dx,dy)
    #one 
    spot = Circle(Point(4,17),.15)
    spot.setFill('black')
    spot.setOutline('black')
    spot.draw(win)
 
    diceList = [(-1.6,-.65),(-1.1,-1.4),(-.5,-2.2), (1.4,-1),(.6,-2),(2.3,-3),
                (3.7,-3),(2,-4.05),(2,-4.9),(1.5,-3.8),(2.5,-5.15),(1.5,-4.65),
                (2.5,-4.3),(3.4,-4.4),(4.5,-4.7),(4.4,-3.9),(3.5,-5.2),(5,-6),
                (5,-6),(7,-6),(6.5,-8),(7.5,-7),(4.5,-6.75),(4.5,-7.25),
                (4.5,-7.75),(5.5,-7.3),(5.5,-7.8),(5.5,-8.3),(10,-9),(8,-9),
                (9,-9.5),(9,-8.5),(8,-10.5),(10.5,-9.9),(9.5,-11.2),
                (11,-12),(13,-12),(12,-12),(12,-11.5),(12,-12.5),
                (11.1,-13.5),(12.4,-13.3),(12.4,-14.2),(13.6,-12.7),(13.6,-13.6)]
 
    for i in  range(len(diceList)):
         
         dx,dy = diceList[i]
         spots = spot.clone()
         spots.draw(win)
         spots.move(dx,dy)
         
    win.getMouse()
    win.close()
 
main()

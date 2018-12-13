# face.py
# Created 12/13/18 by Jenna Folsom
# A program that draws a face

from graphics import *
 
win = GraphWin('Smiley Faces', 400, 400)
win.setBackground('white')
win.setCoords(0, 0, 400, 400)
 
def drawFace(center, size,window):
    
    # draws a head
    head = Circle(center,size*20)
    head.setFill("tan")
    head.draw(win)
    
    # draws a mouth
    mouth = Circle(center, size*13)
    mouth.setFill("pink")
    mouth.setOutline("pink")
    mouth.draw(win)
    smile = Circle(center, size*14)
    smile.move(0,size*4)
    smile.setFill("tan")
    smile.setOutline("tan")
    smile.draw(win)
    
    # draws an eye then doubles it
    eye = Circle(center, size*3)
    eye.move(-size*8,size*6)
    eye.setFill('white')
    eye.draw(win)
    eye2 = eye.clone()
    eye2.draw(win)
    eye2.move(size*16, 0)
    
    # draws a pupil then doubles it
    pupil = Circle(center,size)
    pupil.move(-size*9,size*7)
    pupil.setFill('black')
    pupil.draw(win)
    pupil2 = pupil.clone()
    pupil2.draw(win)
    pupil2.move(size*16,0)
    
    # draws a nose
    nose = Circle(center,size*3)
    nose.move(0,-size*2)
    nose.setOutline('brown')
    nose.setFill('brown')
    nose.draw(win)
 
def main():
 
    i = 0
    for i in range (0,2):
        center = Point(-50+i*85,-50+i*90)
        Face = drawFace(center,3-(i*.5),win)
 
    message.draw(win)
    win.getMouse()
    win.close()
 
main()

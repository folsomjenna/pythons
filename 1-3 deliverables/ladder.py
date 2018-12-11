# ladder.py
# Created on 12/11/18 by Jenna Folsom
# A program that determines the length of a ladder required given a height when leaned against a house

def main():

    import math

    # This is an introduction
    print("This is a program that determines the length of a ladder required given a height when leaned against a house.")

    # This is an input
    height = eval(input("What is the height of the ladder? "))
    angle = eval(input("what is the angle of the ladder? "))
    radians = math.pi / 180 * angle
    length = round(abs((height) / math.sin(radians)) , 2)


    # This is an output
    print("The length of the ladder is", length, ".")

main()    

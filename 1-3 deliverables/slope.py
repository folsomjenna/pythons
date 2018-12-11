# slope.py
# Created on 12/11/18 by Jenna Folsom
# A program that calculates the slope of a line through two (non-vertical) points entered by the user

def main():

    import math

    # This is an introduction
    print("This is a program that calculates the slope of a line through two (non-vertical) points entered by the user.")
    print("                                                                                                            ")   

    # This is an input
    x1 = eval(input("What is the x in the first set of coordinates? "))
    x2 = eval(input("What is the x in second set of coordinates? "))
    y1 = eval(input("What is the y in the first set of coordinates? "))
    y2 = eval(input("Finally, what is the y in the second set of coordinates? "))
    slope = (y2 - y1) / (x2 -x1)

    # This is an output
    print("The slope of the two coordinates is", slope, ".")

main()    

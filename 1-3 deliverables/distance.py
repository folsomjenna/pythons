# distance.py
# Created on 12/11/18 by Jenna Folsom
# A program that calculates the distance of two coordinates given by the user

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
    distance = round(math.sqrt((x2-x1)**2 + (y2-y1)**2) , 2)

    # This is an output
    print("The distance of the two coordinates is", distance, ".")

main()   

# triangle.py
# Created on 12/11/18 by Jenna Folsom
# A program to calculate the area of a triangle given the length of its three sides: a, b, and c

def main():

    import math

    # This is an introduction
    print("This is a program that calculates the area of a triangle given the length of its three sides: a, b, and c.")

    # This is an input
    a = eval(input("What is the length of side a? "))
    b = eval(input("What is the length of side b? "))
    c = eval(input("what is the length of side c? "))
    s = (a + b + c) / 2
    A = round(math.sqrt(s*(s - a) * (s - b) * (s - c)) , 2)

    # This is the output
    print("The area of the triangle is", A, ".")

main()    

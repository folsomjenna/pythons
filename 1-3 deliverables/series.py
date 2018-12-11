# series.py
# Created on 12/11/18 by Jenna Folsom
# A program to sum a series of numbers given by the user

def main():

    import math

    # This is an introduction
    print("This is a program to sum a series of numbers given by you.")

    # This is an input
    numbers = eval(input("How many numbers would you like to be summed? "))
    v = 0
    for i in range(numbers):
        x = eval(input("Enter number: "))
        v = x + v

    # This is an output
    print("The sum of your", numbers, "numbers is", v,".")
    
main()    

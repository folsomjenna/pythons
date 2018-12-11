# fibonacci.py
# Created on 12/11/18 by Jenna Folsom
# A program that computes the fibonacci sequence by the number of the value the user inputs

def main():

    import math

    # This is an introduction
    print("This is a program that computes the fibonacci sequence by the number of the value that you input.")
    
    # This is an input
    n = eval(input("How many terms would you like to sum? "))
    x = 0
    y = 1
    for i in range(n):
        x, y = y, x + y
        print(x)
main()        

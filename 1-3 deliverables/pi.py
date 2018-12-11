# pi.py
# Created on 12/11/18 by Jenna Folsom
# A program that approximates the value of pi by summing the terms

def main():

    import math

    # This is an introduction
    print("This is a program that approximates the value of pi by summing the terms.")

    # This is an input
    n = eval(input("How many terms would you like to sum? "))
    x = 0
    for i in range(n):
        x = x + 4.0 * (-1) ** i / (2 * i + 1)
        print(x)
main()        
        

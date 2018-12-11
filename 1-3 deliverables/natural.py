# natural.py
# Created on 12/11/18
# A program to find the sum of the first n natural numbers.

def main():

    import math

    # This is an introduction
    print("This is a program to find the sum of the first n natural number.")

    # This is an input
    n = eval(input("What would you like to find the sum of? "))
    t = 0
    a = 1

    # This is an output
    for i in range(n):
        t = t + a
        a = a + 1

    print("The sum of the first natural numbers is", t, ".")

main()    

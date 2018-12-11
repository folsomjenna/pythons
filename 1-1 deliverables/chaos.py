# File: chaos.py
# Created 11/19/18 by Jenna Folsom
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("Now how many values would you like to be displayed: "))
    for i in range(n) :
        x = 2.0 * x * (1 - x)
        print(x)
main()        

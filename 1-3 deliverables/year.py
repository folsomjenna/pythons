# year.py
# Created on 12/11/18 by Jenna Folsom
# A program that prompts the user for a 4-digit year and then outputs the value of the epact

def main():

    import math

    # This is an introduction
    print("This is a program that prompts you for a 4-digit year and then outputs the value of the epact.")

    # This is an input
    year = eval(input("What 4-digit year would you like to use? "))
    C = year//100
    epact = (8 + (C//4) - C + ((8*C + 13)//25) + 11 *(year%19)) %30

    # This is an output
    print("The value of the epact is", epact, ".")

main()    

# coffee.py
# Created on 12/11/18 by Jenna Folsom
# A program that calculates a cost of an order at Konditorei Coffee Shop

def main():

    import math

    # This is an introduction
    print("This program is used to calculate the cost of an order at Konditorei Coffee Shop.")

    # This is an input
    pounds = eval(input("How many pounds of coffee did you buy? "))
    cost = pounds * 10.50
    ships = (pounds * 0.86) + 1.50
    total = cost + ships

    # This is an output
    print("The cost of an order for", pounds, "pounds is", total, "dollars.")

main()    

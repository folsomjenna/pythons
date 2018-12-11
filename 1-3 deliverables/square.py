# square.py
# Created on 12/10/18 by Jenna Folsom
# A program that calculates the cost per square inch of a circular pizza

def main():

    import math

    # this is in an introduction
    print("This program is used to calculate the cost per square inch of a circular pizza.")

    # this is an input
    cost = eval(input("Enter the cost of the pizza: "))
    diameter = eval(input("Now enter the diameter of the pizza: "))
    area = math.pi * diameter / 2
    square = (area) ** 2
    per = round(cost / square , 2)                

    # this is an output
    print("The cost per square inch is about $",per,".")

main()                    
                    

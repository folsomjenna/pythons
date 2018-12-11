# thunder.py
# Created 12/10/18 by Jenna Folsom
# A program that determines the distance to a lightning strike based on the time elapsed between the flash and the sound of thunder

def main():

    import math

    # this is an introduction
    print("This is a program that determines the distance to a lightning strike")
    print("based on the time elapsed between the flash and the sound of thunder.")
    print("                                                                     ")

    # this is an input
    distance = eval(input("How many seconds were between the flash and the sound of thunder? "))
    total = distance * 1100
    miles = round(total / 5280 , 2)

    # this is an output
    print("The distance to the lightning strike is", miles, "miles.")

main()                    

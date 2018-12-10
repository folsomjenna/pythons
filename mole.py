# mole.py
# Created on 12/10/18 by Jenna Folsom
# A program that computes the molecular weight of a carbohydrate (in grams per mole)

def main():

    import math

    # this is an introduction
    print("This program is used to compute the molecular weight of a carbohydrate (in grams per moles)")

    # this is an input
    hydrogen = eval(input("Enter the amount of hydrogen atoms in the molecule: "))
    carbon = eval(input("Enter the amount of carbo atoms in the molecule: "))
    oxygen = eval(input("Enter the amount of oxygen atoms in the molecule: "))
    total = (hydrogen * 1.00794) + (carbon * 12.0107) + (oxygen * 15.9994)

    # this is an output
    print("The molecular weight is", total,".")

main()                  
                  
    

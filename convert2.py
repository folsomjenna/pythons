# convert2.py
# Created 11/20/18 by Jenna Folsom
# A program to convert distances measured in kilometers to miles

def main():
    
    print("This program converts distances measured in kilometers to miles.")
    
    kilometers = eval(input("What is the distance in kilometers?"))
    miles = kilometers * .62
    
    print("The distance is", kilometers * .62, "miles.")
    input("Press the <Enter> key to quit.")

main()    

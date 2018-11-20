# convert.py
# Created on 11/20/18 by Jenna Folsom
# A program to convert Celsius temps to Fahrenheit.

def main():
    #This is a loop
    for i in range(5):
        #This is an introduction
        print("Hey! This is a program to convert Celsius temperatures to Fahrenheit.")
        #This is an input
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9 / 5 * celsius + 32
        #This is an output
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main ()
input("Press the <Enter> key to quit.")

# convert3.py
# Created on 11/20/18 by Jenna Folsom
# A program to convert Fahrenheit temperatures to Celsius.

def main():
        #This is an introduction
        print("Hey! This is a program to convert Fahrenheit temperatures to Celsius.")
        #This is an input
        Fahrenheit = eval(input("What is the Fahrenheit temperature? "))
        Celsius = (Fahrenheit - 32) * 5/9
        #This is an output
        print("The temperature is", Celsius, "degrees Celsius.")

main()
input("Press the <Enter> key to quit.")

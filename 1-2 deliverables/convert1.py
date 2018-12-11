# convert1.py
# Created on 11/20/18 by Jenna Folsom
# Computes and prints a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees from 0°C to 100°C.

def main():
    print("Celisus Temperatures and")
    print("Their Fahrenheit Equivalents")
    print("                            ")
    print("{0:<14}{1:<14}".format("Celsius", "Fahrenheit"))
    print("----------------------------")
    for i in range(11):
        celsius = 10 * i
        fahrenheit = int(9/5 * celsius + 32)
        print("{0:<14}{1:<14}".format(celsius, fahrenheit))
main()

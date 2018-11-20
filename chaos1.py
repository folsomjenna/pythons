# chaos1.py
# Created 11/19/18 by Jenna Folsom
# A simple program illustrating chaotic behavior (part 6a of 1-1).

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100) :
        x = 3.9 * x * (1 - x)
        print(x)
main()   

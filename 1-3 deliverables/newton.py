# newton.py
# Created on 12/12/18 by Jenna Folsom
# A program that calculates the square root based off of Newton's Method

def main():

    import math

     # This is an introduction
     print("This program caluculates the square root based off of the Newton's Method.")
    
     # This is an input
     x = eval(input("What would you like to sqaure root? "))
     guess = eval(input("How many times would you like this to loop to improve the guess? "))
     
     for i in range(guess):
         top = guess + x / guess
         final_x = float(top) / 2


     close = final_x - math.sqrt(x)
     close_two = math.sqrt(x)

     # This is an output
     print("The guess is", final_x, "which is", close, "away from", close_two)

main()

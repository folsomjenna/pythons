# futval.py
# Created on 11/20/18 by Jenna Folsom
# A program to compute the future value of an investment
# with number of years determined by the user.

def main():
    #This is an introduction
    print("This program calculates the total future value of a multi-year investment with")
    print("describing the interest accrued in terms of a nominal rate and the number of compounding periods.")

    #These are inputs
    principal = eval(input("Enter the initial principal: "))
    interestrate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding periods per year: "))
    years = eval(input("Enter the number of years for the investment: "))

    nominalrate = interestrate / periods

    #This is a loop      
    for i in range(periods * years):
          principal = principal * (1 + nominalrate)

    print("The value in", years ,"years is:", principal, sep=" ")

main()

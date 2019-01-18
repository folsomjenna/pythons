# quiz.py
# Created by Jenna Folsom on 1/17/19
# Converts a quiz score from 1-5 to the corresponding grade.

def main():
    # This is an intro
    print("This program accepts quiz grades and prints out the corresponding grades.")
    
    # Create list of possible letter grades
    lettergradescale = "FFDCBA"
    
    # Prompt user for quiz grade
    quizgrade = int(input("Please enter the quiz grade on a scale from 0 to 5: "))
    lettergrade = lettergradescale[quizgrade]

    # This is an outro
    print("Your quiz grade of {0} corrsesponds to the letter grade of {1}.".format(quizgrade, lettergrade))

main()    

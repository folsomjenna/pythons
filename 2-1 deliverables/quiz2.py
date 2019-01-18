# quiz2.py
# Created by Jenna Folsom on 1/17/19
# Converts a quiz score from 0-100 to the corresponding grade.

def main():
    # This is an intro
    print("This program converts a quiz score from 0-100 to the corresponding grade.")

    # This is an input
    lettergradescale = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDCCCCCCCCCCBBBBBBBBBBAAAAAAAAAAA"
    examgrade = int(input("Please enter the quiz grade on a scale from 0 to 100: "))
    lettergrade = lettergradescale[examgrade]

    # This is an output
    print("Your grade of {0} corresponds to the letter grade of {1}.".format(examgrade, lettergrade))

main()

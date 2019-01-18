# letters.py
# Created by Jenna Folsom on 1/18/19
# This program counts the amount of words in a sentence.

def main():
    # This is an intro.
    print("This is a program that counts the amount of letters in a sentence.")

    # This is an input
    phrase = input("Enter a sentence: ")
    words = phrase.split() #Forget ()
    wordCount = len(words)

    # This is an output
    print("The total word count is: %s" % wordCount)
    
main()

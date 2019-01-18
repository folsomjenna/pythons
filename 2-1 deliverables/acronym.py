# acronym.py
# Created by Jenna Folsom on 1/17/19
# Allows user to type in a phrase and then outputs acronym.

def acronym(Phrases):
    #This is an intro
    print("This program outputs an acronym for a phrase given by a user.")

    # This is an input
    acronym = ("")
    for word in Phrases.split():
        acronym = acronym + word[0].upper()
    return acronym


# Program derives Acronyms from phrases
def main():

    # Description
    print("Program derives Acronyms from phrases.")
    
    # Recieve phrase input
    Phrases = input("Please input your phrase to convert: ")

    # This is an output 
    print(acronym(Phrases))
    
main()

# words.py
# Created by Jenna Folsom on 1/18/19
# This program counts the amount of words in a sentence.

def main():
    # This is an input
    print("This program calculates the average word length in a sentence.")
    sent = input("What is the sentence? ")
    
    #Calculates number of words
    sentlist = sent.split()
    total = len(sentlist)
    
    sum = 0
    for word in sentlist:
      sum += len(word) 

    # This is an output
    avg = sum / total
    print(avg)

main()

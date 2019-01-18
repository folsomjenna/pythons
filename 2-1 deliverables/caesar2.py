# caesar2.py
# Created by Jenna Folsom on 1/18/19
# This program can adds a loop to the Caesar cipher.

def main():
    # This is an intro.
    print("This program can encode and decode Caesar ciphers along with a loop.")

    # This is an input
    text = input("Enter text to encode: ").lower()
    key = eval(input("Enter the value of the key: "))
    textList = text.split()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
 
    codelist = []
  
  # Encode message

    for word in textList:
          encrypt = ("")
    for ch in word:
        index = (ord(ch) - ord('a') + key) % 26
        encrypt = encrypt + alphabet[index]
        
        
    codelist.append(encrypt)

  # This is an output
    print(' '.join(codelist))

main()

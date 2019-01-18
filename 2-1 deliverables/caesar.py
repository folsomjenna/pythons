# caesar.py
# Created by Jenna Folsom on 1/18/19
# This program can encode and decode Caesar ciphers.

def main():

    # This is an intro.
    print("This program can encode and decode Caesar ciphers.")

    message = input("What is the message? ")
    key = eval(input("What is the key(1-25)? "))
    messagelist = message.upper().split()
  
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
    codeList = []
    for word in messagelist:
      code = ""
      for ch in word:
          index = (ord(ch) - ord('A') + key) % 26
          code += letters[index]
      codeList.append(code)

    # This is an output
    print(' '.join(codeList))
    
main()  

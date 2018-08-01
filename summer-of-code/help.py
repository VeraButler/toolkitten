import os
textfile = open('C:/users/verab/documents/toolkitten/summer-of-code/week-02/alice_in_wonderland.txt','r', encoding="utf8" ) 
from string import ascii_lowercase 

def count_letters(text):
    for letter in ascii_lowercase:
        count = 0
        #letters = []
        for line in text:
            for char in line:
                if char == letter:
                    count += 1
        print (letter + ' : ' + str(count))
    break;

inputfile = textfile.read()
print(count_letters(inputfile))
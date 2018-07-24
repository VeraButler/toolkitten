#Make a function that returns n number of moo's


#functions, parameters
#def moo(n):
    #print('moo ' * (n + 1))
    #return 'moo' * n
#moo(3)

#for i in range(1, 4):
    #moo(i)

#Recusive Function
def ask_recursively(question):
    print(question)
    reply = input('> ').lower()
    if reply == 'yes':
        return True
    if reply == 'no':
        return False
    else:
        print('Please answer "yes" or "no".')
        ask_recursively(question)
ask_recursively("Do you wet the bed?")

#Testing
    #import unittest
    #from file_name import function

#Reading and writing files
import os
filename =  'C:/Users/verab/Documents/toolkitten/summer-of-code/week-02/alice_in_wonderland1.txt'
file = open(filename, 'r')
#for line in file:
    #print(line)

raw = file.read()
#print('from zero to sixty-five: ' + raw[:65])

#print('AGAIN: ' + raw[0:65])

#print('Length: ' + str(len(raw))  )

#print(raw[:145000])

#calculate a table for each letter in the alphabet from
#a-z and cound how many times each letter appears in the text
#a: ...
#b: ...
#aka frequency distribution
count = 0
from string import ascii_lowercase
for c in ascii_lowercase:
    for n in raw:
        if n == c:
            count = count + 1
        else:
            continue
    print(c + ":" + str(count))
    count = 0

#for   FileNotFoundError: [Errno 2] No such file or directory:
    #import os
    #cwd = os.getcwd()  # Get the current working directory (cwd)
    #files = os.listdir(cwd)  # Get all the files in that directory
    #print("Files in '%s': %s" % (cwd, files))
    #***OR ENTER ABS PATH***
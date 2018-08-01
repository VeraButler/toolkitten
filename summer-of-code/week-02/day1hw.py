import os
filename = 'C:\\Users\\verab\\Documents\\toolkitten\\summer-of-code\\week-02\\aliceInWonderland.txt'
file = open(filename, "r", encoding = "utf8")
raw = file.read()

#count letters in range

#if letters match chr(i) count += count
import itertools as it
count = 0
for i in it.chain(range(65, 89), range(97, 121)):
    if i <= 89:
       for chr(i) in raw[line]:
           count += count
    if i >= 97:
        count = count + 1
    print(chr(i) + ": " + str(count))


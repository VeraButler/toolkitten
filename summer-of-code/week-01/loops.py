#loops
# text = ""

# while text != "bye":
#   text = input("say something please")
#   print("you said " + text + ".")

#   if text == "bye":
#     print("good bye to you too")
#     break

# while text != "bye":
#   text = input("say something please : ")
#   print("You said \"" + text + "\".")
#   print('You said "' + text + '".')


# print("good bye to you too")


# i = 1
# while i < 11:
#   print(i)
#   i = i + 1

# j = 0
# while j < 11:
#   print(j)
#   if j == 3:
#     break
#   j += 1

# for x in range(10):
#   print(x)

# for x in range(5, 10):
#   print(x)

# for x in range(5, 50, 3):
#   print(x)

# students = ["Rocio Pena", "Kat Burkinshaw", "Archana Kumari", "Christina Tarantino", "Jessi_RS","Elle J", "libi", "t. pspisilova", "F. Margharita Wailes-Fairbairn"]

# for s in students:
#   if len(s) > 7:
#     print(s + " is an amazing Pythonista and has a very long name!")
#     if len(s) > 20:
#       print("Supercalifragilisticexpialidocious!")
#   elif len(s) == 6:
#     print(s + " is an amazing Pythonista and has a name that's exactly 6 characters long!")
#   elif len(s) == 8:
#     print(s + " is an amazing Pythonista and has a name that's exactly 8 characters long!")
#   else:
#     print(s + " is an amazing Pythonista and a minimalist!")

# for c in characters:

# for m in members:

# for c in cars:

students = ["Rocio Pena", "Kat Burkinshaw", "Archana Kumari", "Christina Tarantino", "Jessi_RS","Elle J", "libi", "t. pspisilova", "F. Margharita Wailes-Fairbairn"]

# for s in students:
#   print(s)

# list comprehension

# usernames = [dosomething(element) for everyelement in list]

# usernames = [print(s) for s in students]
# print(usernames)

# usernames = [s+"@1mwtt" for s in students]
# print(usernames)

# students.append("Marta Bodojra")
# print(students)

# students.pop()
# print(students)
students.sort()
print(students)

fruits = ["orange", 2, "kiwi", {}]
print(fruits)

# 'real array'

#import numpy

#a = numpy.array([1,2,3])
# I = 1, V = 5, X = 10, L = 50, C = 100, D =500, M = 1000
import math

d=0
while((d > 3000) or (d==0)):
    d=int(input("Enter a number between 1 and 3000: "))
rn = ""

decimal=[1000, 5000, 100, 50, 10, 5, 1]
roman=["M", "D", "C", "L", "X", "V", "I"]
i=0
for n in decimal:
    if(d==9):
        rn=rn+"IX"
        break
    if(d==4):
            rn=rn+"IV"
            break
    q= math.floor(d/n)
    r = d % n
    

#Leap Years

#Introduction
print("This program is to find all the leap years between to years.")
#Input starting year
startYear = input("Input the start year: ")
#Input ending year
endYear = input("Input the end year: ")
#Put all leap years between inputs
#Note Years divisible by 100 are not leap years
    #unless also divisible by 400
#years%4 == 0 ==> leap year
startYear = int(startYear)
endYear = int(endYear) + 1
print(startYear)
divFourHun = 0
for i in range(startYear, endYear):
    if i%4 == 0:
        if i%400 == 0:
            divFourHun == 1
        if i%100 == 0 and divFourHun == 0:
            continue
        print(i)

#we'll use sys library to be able to access and use command line arguments
import sys

n = len(sys.argv)           #just to know how many elemts we have to loop around
if n > 1:                   #to avoid an err in case there r no args
    sum = sys.argv[1]       #a var to hold the whole shit
    for i in range(2, n):
        sum += " " + sys.argv[i]
    print(((sum).swapcase())[::-1])

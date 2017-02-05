import random
import sys

def func():
    x = random.randint(1, 100)
    n = 0
    while n != x:
        n = int(input("Try to guess the number from 1 to 100: "))
        if n % 1 != 0:
            print ("You write not an integer number!")
            sys.exit()
        if n < x:
            print ("X is more than " + str(n))
        elif n > x:
            print ("X is less than " + str(n))
    print ("Congratulations! You have guess. X = " + str(n))

func()

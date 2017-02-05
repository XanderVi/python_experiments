import random
import sys

def func():
    top = float(input("Write the top of interval: "))
    if top % 1 != 0:
            print ("You write not an integer number!")
            sys.exit()
    bot = float(input("Write the bottom of interval: "))
    if bot % 1 != 0:
            print ("You write not an integer number")
            sys.exit()
    step = float(input("Write the step of interval: "))
    if step % 1 != 0:
            print ("You write not an integer number")
            sys.exit()
    a = random.randint(bot, top)
    while a<=(top-step):
        a += step
    while a >= bot:
        print (a)
        a -= step

func()

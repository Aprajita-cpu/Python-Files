from random import randint
from time import sleep

heads=0
tails=0
print("Assignment 2 CS-808")
print("Sample space={Head,Tail}")
flip=int(input("How many times,you want to toss the coin:"))

for i in range(flip):
    result=randint(0,1)
    sleep(1)
    if result==0:
        print("Heads")
        heads += 1
    else:
        print("Tails")
        tails +=1

print("The results are:")
print("Heads",heads)
print("Tails",tails)

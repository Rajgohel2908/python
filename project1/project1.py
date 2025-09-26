'''
-1 = snake
0 = water
1 = gun
'''
import random

revdct = {-1: "snake", 0: "Water", 1: "gun"}
dct = {"snake": -1, "water": 0,"gun" : 1}
com = random.choice((-1,0, 1))
userchoice = input("Enter your choice :")

user = dct[userchoice]
print(f"you choosed {revdct[user]} \ncomputer choosed {revdct[com]}")

if(com==user):
    print("Tie!")
else:
    if((user==1 and com==-1) or (user==0 and com==1) or (user==-1 and com==0)):
        print("you won!")
    elif((com==1 and user==-1) or (com==0 and user==1) or (com==-1 and user==0)):
        print("you lose!")
    else:
        print("something went wrong!")
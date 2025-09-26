from random import randint

n = randint(1,50)
a = 0
guesses = 1
while(a != n):
    a = int(input("guess the number between(1-50):"))
    if(a == n):
        print(f"you guessed the number {n} in {guesses} attempts!")
        break
    elif(a > n):
        print("guess lower number")
    elif(a < n):
        print("guess higher number")
    guesses += 1
import random

def game():
    print("Game started!!!!")
    score = random.randint(1, 100)
    print(f"Your score :{score}")
    with open("hi-score.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    if(score>hiscore):
        with open("hi-score.txt", "w") as f:
            f.write(str(score))

game()
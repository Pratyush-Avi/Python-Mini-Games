from random import randint
start = 1
end = 1000
value = randint(start, end)
print("The computer choose a number between", start, "and", end)
guess = None
while guess!=value:
    text=input("Guess the Number: ")
    guess=int(text)

    if guess <value:
        print("The number is Higher")
    elif guess >value:
        print("The number is lower")

print("Congratulation!!! You guessed the number, You won.")

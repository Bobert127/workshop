from random import randint

draw = randint(1, 10)

try:
    number = int(input("Guess the number: "))
except ValueError:
    print("It's not a number!")

while draw == number:
    if draw == number:
        print("You win!")
    elif draw > number:
        print("To small!")
    elif draw < number:
        print("To big!")

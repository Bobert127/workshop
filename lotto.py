import random
from random import randint


def check_number():
    while True:
        try:
            input_number = int(input("Podaj liczbę z zakresu 1-49: "))
            break
        except ValueError:
            print("It's not a number!")
    return input_number


def check_numbers():
    input_numbers = []
    while len(input_numbers) < 6:
        number = check_number()
        if number not in input_numbers and 0 < number < 50:
            input_numbers.append(number)
    return input_numbers


def list_numbers():
    print(", ".join(str(input_numbers) for input_numbers in sorted(input_numbers)))

def lotto_numbers():
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    return numbers[:6]

def lotto():
    mine_number = check_numbers()
    print("Your type: ")
    print_numbers(mine_number)

    lotto_number = lotto_numbers()
    print("Lotto numbers: ")
    print_numbers(lotto_number)

    a = 0
    for


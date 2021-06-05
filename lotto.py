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
        #if number not in input_numbers and 0 < number < 50:
        if number not in input_numbers and 0 < number <= 49:
            input_numbers.append(number)
    return input_numbers


def list_numbers(numbers):
    print(", ".join(str(number) for number in sorted(numbers)))

def lotto_numbers():
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    return numbers[:6]

def lotto():
    mine_number = check_numbers()
    print("Your type: ")
    list_numbers(mine_number)

    lotto_number = lotto_numbers()
    print("Lotto numbers: ")
    list_numbers(lotto_number)

    a = 0
    for mine_number in mine_number:
        if mine_number in lotto_number:
            a += 1
    print(f"Your type {a} {'mine_number' if a == 1 else 'mine_number'}")

if __name__ == '__main__':

    lotto()


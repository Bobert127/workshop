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
        if number not in input_numbers and 0 < number <== 49:
            input_numbers.append(number)

    return input_numbers



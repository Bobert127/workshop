from random import randint
def check_number():

    while True:
        try:
            input_number = input("Podaj liczbę z zakresu 1-49: ")
            break
        except ValueError:
            print("It's not a number!")
    return input_number





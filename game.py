from random import randint

def init_number():

    while True:
        try:
            number = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")

    return number


def secret_number():
    secret_draw = randint(1, 100)
    input_draw = init_number()
    while secret_draw != input_draw:
        if secret_draw < input_draw:
            print("To big!")
        else:
            print("To small!")
        input_draw = init_number()
    print("You win!")

if __name__ == '__main__':

    secret_number()


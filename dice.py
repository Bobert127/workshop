import random

dice = ("D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3")


def my_funcjion(my_cod):
    for e in dice:
        if e in my_cod:
            multi, modi = my_cod.split(e)
        e_value = int(e[1:])
        break
    else:
        return "Wrong Input"
        multi = int(multi) if multi else 1
        modi = int(modi) if modi else 0

    return sum([random.randint(1, e_value) for _ in range(multi)]) + modi


if __name__ == '__main__':
    print(my_funcjion("2D10+10"))

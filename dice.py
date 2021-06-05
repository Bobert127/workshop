import random

dice = ("D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3")


def my_funcjion(my_cod):
    for e in dice:
        if e in my_cod:
            try:
                my, mr = my_cod.split(e)
            except ValueError:
                return "Wrong"
            e_value = int(e[1:])
            break
    else:
        return "Wrong"
    try:
        my = int(my) if my else 1
    except ValueError:
        return "wrong"
    try:
        mr = int(mr) if mr else 0
    except ValueError:
            return "wrong"
    return sum([random.randint(1, e_value) for _ in range(my)]) + mr


if __name__ == '__main__':
    print(my_funcjion("5D10+8"))


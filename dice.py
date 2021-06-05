import random

dice = ("D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3")


def my_funcjion(my_cod):
    for e in dice:
        if e in my_cod:
            my, mr = my_cod.split(e)
        e_value = int(e[1:])
        #break
    #else:
        #return "Wrong Input"
    my = int(my) if my else 1
    mr = int(mr) if mr else 0

    return sum([random.randint(1, e_value) for _ in range(my)]) + mr


if __name__ == '__main__':
    print(my_funcjion("2D10+10"))

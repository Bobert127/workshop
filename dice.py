import random

dice = ("D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3")

def my_funcjion(my_cod):
    for e in dice:
        if e in my_cod:
            multi, mody = my_cod.split(e)
        e_value -= int(e[1:])
        break
    else:
        return "Wrong Input"
#print(dice[1])




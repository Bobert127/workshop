def mine_input():
p_input = ["to small", "to big", "you win"]
     while True:
        answer = input().lower()
        if ansver in p_input:
            break
        print("Input not in ["to small", "to big", "you win"]")
    return answer

def mine_number():
    print("your number between 0 and 1000!")
    print("Pres 'Enter' to continue")
    input()
    min = 0
    max = 1000
    answer = ""
    while answer != "you win":
        try_find = (max - min) // 2 + min
        print(f"Your number is: {try_find}")
        answer = mine_input()


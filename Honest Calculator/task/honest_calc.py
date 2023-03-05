def extra_one(res, memory):
    msg = ["Are you sure? It is only one digit! (y / n)",
           "Don't be silly! It's just one number! Add to the memory? (y / n)",
           "Last chance! Do you really want to embarrass yourself? (y / n)"]
    msg_index = 0
    while True:
        print(msg[msg_index])
        odp = input()
        if odp == 'y':
            if msg_index >= 2:
                break
            msg_index += 1
        elif odp == 'n':
            return memory
    return res


def is_one_digit(v):
    v = float(v)
    return v > -10 and v < 10 and v.is_integer()


def check(v1, v2, v3, msg_6, msg_7, msg_8, msg_9):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if v1 == 1 or v2 == 1 and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 in ['+', '*', '-']):
        msg += msg_8
    if msg != "":
        print(msg_9 + msg)


def format_input(msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, memory, msg_6, msg_7, msg_8, msg_9):
    while True:
        print(msg_0)
        x = input()
        l = x.split()
        if l[0] == 'M':
            first = memory
        else:
            try:
                first = float(l[0])
            except ValueError:
                print(msg_1)
                continue

        if l[2] == 'M':
            second = memory
        else:
            try:
                second = float(l[2])
            except ValueError:
                print(msg_1)
                continue
        if l[1] not in ['+', '-', '*', '/']:
            print(msg_2)
            continue
        check(first, second, l[1], msg_6, msg_7, msg_8, msg_9)

        if l[1] == '+':
            res = first + second
        elif l[1] == '-':
            res = first - second
        elif l[1] == '*':
            res = first * second
        elif l[1] == '/' and str(second) != "0":
            res = first / second
        else:
            print(msg_3)
            continue
        print(res)
        while True:
            print(msg_4)
            odp = input()
            if odp == 'y':
                if is_one_digit(res):
                    memory = extra_one(res, memory)
                else:
                    memory = res
                break
            else:
                if odp != 'n':
                    continue
                else:
                    break
        while True:
            print(msg_5)
            odp = input()
            if odp == 'y':
                break
            else:
                if odp != 'n':
                    continue
                else:
                    return


def main():
    memory = 0
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = "Yeah... division by zero. Smart move..."
    msg_4 = "Do you want to store the result? (y / n):"
    msg_5 = "Do you want to continue calculations? (y / n):"
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    format_input(msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, memory, msg_6, msg_7, msg_8, msg_9)


if __name__ == "__main__":
    main()
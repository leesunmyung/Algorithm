# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):

    global str
    global remain_A
    global remain_B

    str = ''
    remain_A = A
    remain_B = B

    if (A >= B):
        while ((remain_A != 0) or (remain_B != 0)):
            print_A_twice()
            print_B_twice()

    else:
        while ((remain_A != 0) or (remain_B != 0)):
            print_B_twice()
            print_A_twice()
    return str


def print_A_twice():
    global str
    global remain_A
    for i in range(0, 2):
        if (remain_A != 0):
            str = str + 'a'
            remain_A -= 1

def print_B_twice():
    global str
    global remain_B
    for i in range(0, 2):
        if (remain_B != 0):
            str = str + 'b'
            remain_B -= 1

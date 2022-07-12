# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    flag = [0 for i in range(0, len(A)+2)]

    for i in range(0, len(A)):
        flag[A[i]] = 1

    return flag.index(0, 1)

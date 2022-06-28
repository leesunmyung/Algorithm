# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    next_index = 0
    length = 0
    flag = [0 for i in range(len(A))]

    while True:
        if next_index == -1:
            break
        else:
            flag[next_index] = 1
            next_index = A[next_index]
            length += 1

    
    count = 0
    for i in range(0, len(flag)):
        if flag[i] == '0':
            count += 1

    return length + count
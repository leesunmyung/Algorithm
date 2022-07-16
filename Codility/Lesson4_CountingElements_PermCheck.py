# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    sorted_A = A.sort()

    num = A[0]

    for i in range(0, len(A)):
        if (num == A[i]):
            num += 1
        else:
            return 0
            
    return 1
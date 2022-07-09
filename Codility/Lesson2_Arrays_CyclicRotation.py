# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    
    rotated_A= [0 for i in range(0, len(A))]

    num = K % len(A)

    if (num == 0):
        return A
        
    for i in range(0, len(A)):

        if (i <= num - 2):
            rotated_A[num+i] = A[i]

        else:
            rotated_A[i-(num-1)] = A[i]

    return rotated_A

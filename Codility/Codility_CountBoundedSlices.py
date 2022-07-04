# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):

    count = 0

    for i in range(0, len(A)):

        for j in range(i, len(A)):

            if ((max(A[i:j+1]) - min(A[i:j+1])) <= K):
                count += 1
    
    return count
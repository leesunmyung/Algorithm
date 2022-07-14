# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    array0 = []
    array1 = []

    for i in range(0, len(A)):
        if (A[i] == 0):
            array0.append(i)
        else:
            array1.append(i)

    count = 0
    for i in range(0, len(array0)):
        for j in range(0, len(array1)):
            if ((array0[i] >= 0) and (array0[i] < array1[j]) and (array1[j] < len(A))):
                count += 1
    
    return count
    

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):

    bin_A = str(format(A, 'b'))
    bin_B = str(format(B, 'b'))
    bin_C = str(format(C, 'b'))

    number = 0

    num0_index = []

    for i in range(0, len(bin_A)):
        if (bin_A[i] == '0'):
            num0_index.append(i)
    
    
    for i in range(0, len(bin_B)):
        if (bin_B[i] == '0'):
            num0_index.append(i)
  
    for i in range(0, len(bin_C)):
        if (bin_C[i] == '0'):
            num0_index.append(i)

    num0_index_set = set(num0_index)
    num0_index_count = len(num0_index_set)
    number = pow(2, num0_index_count-1)

    return number

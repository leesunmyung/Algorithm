# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):

    word_list = S.split(' ')

    max_word = ''
    
    for word in word_list:

        letter = 0
        digit = 0
        etc = 0

        for i in word:

            if (i.isdigit()):
                digit += 1   

            elif ((ord(i) >= 65) and (ord(i) <= 90)) or ((ord(i) >= 97) and (ord(i) <= 122)):
                letter += 1

            else:
                etc += 1

        if ((digit % 2 == 1) and (letter % 2 == 0) and (etc == 0)):
            
            if (len(word) > len(max_word)):
                max_word = word
    
    return len(max_word) if (max_word != '') else -1
        
            

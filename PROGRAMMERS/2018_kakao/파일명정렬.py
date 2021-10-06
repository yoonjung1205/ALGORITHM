def solution(files):
    answer = []

    
    result = []
    
    for file in files:
        head = ''
        number = ''
        tail = ''
        
        flag_number = 0
        flag_tail = 0
        for alpha in file:
            '''if alpha.isalpha() and flag_number == 0 and flag_tail == 0:
                head += alpha
            elif alpha in ' .-' and flag_number == 0 and flag_tail == 0:
                head += alpha
            elif alpha.isdecimal():
                flag_number = 1
                number += alpha'''
            
            if alpha.isdecimal() and not flag_tail:
                flag_number = 1
                number += alpha
            elif not flag_number and not flag_tail:
                head += alpha
            else:
                flag_tail = 1
                tail += alpha
        result.append([head,number,tail])
    result.sort(key=lambda x: (x[0].lower(),int(x[1])))
    for i in range(len(result)):
        answer.append("".join(result[i]))
    print(head)
    print(number)
    print(tail)
    print(result)
    
    return answer
files =  ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
solution(files)
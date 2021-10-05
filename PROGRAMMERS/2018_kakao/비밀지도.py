def solution(n, arr1, arr2):
    b_arr1 = []
    b_arr2 = []
    for i in range(n):
        b1 = bin(arr1[i])[2:]
        if len(b1) == n:
            b_arr1.append(b1)
        else:
            b1 = ('0'*(n-len(b1)))+b1
            b_arr1.append(b1)
            
    for i in range(n):
        b2 = bin(arr2[i])[2:]
        if len(b2) == n:
            b_arr2.append(b2)
        else:
            b2 = ('0'*(n-len(b2)))+b2
            b_arr2.append(b2)
    
    answer = ['' for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if b_arr1[i][j] =='1' or b_arr2[i][j]=='1':
                answer[i] += '#'
            else:
                answer[i] += ' '
                
    return answer
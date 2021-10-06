# 10진수 -> n진수
def N_notation(number,N):
    T = "0123456789ABCDEF"
    q, r = divmod(number, N)    # 몫과 나머지 동시에 저장하는 함수
    if q:
        return N_notation(q,N) + T[r]
    else:
        return T[r]
    
def solution(n, t, m, p):
    answer = ''
    result = []
    # 튜브가 말해야하는 개수 t, 사람 수 m -> 변환해서 저장해야될 값(10진수) <= t*m 
    for i in range(t*m):
        num = N_notation(i,n)   # n진법으로 변환된 값이 저장 ex) i=4, num ='100'
        for elem in num:
            result.append(elem)
    print(result)
    
    start = p-1
    for i in range(start,t*m,m):
        answer += result[i]
    print(answer)
    return answer

solution(2,4,2,1)
solution(16,16,2,1)
solution(16,16,2,2)
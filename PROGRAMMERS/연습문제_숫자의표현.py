def solution(n):
    answer = 0
    
    for i in range(1,n+1):    
        s = i
        total = 0
        while True:
            total += s
            if total > n:
                break
            elif total == n:
                answer += 1
            s += 1
    
    return answer
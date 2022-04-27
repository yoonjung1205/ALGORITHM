def solution(s):
    answer = 0
    result = []    
    for i in range(len(s)):
        if len(result) == 0:
            result.append(s[i])
        elif result[-1] == s[i]:
            result.pop()
        else:
            result.append(s[i])
    
    if len(result) == 0:
        answer = 1
    return answer
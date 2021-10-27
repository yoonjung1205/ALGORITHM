def solution(relation):
    def choice(cur):
        if cur == m:
            arr2 = arr[::]
            result.append(arr2)
            return
        
        for i in range(2):
            arr[cur] = i
            choice(cur+1)
        
        
    answer = 0
    # 4가지 중에서 고를 수 있는 모든 경우의 수 구한 후
    # 그 때 중복되는 것이 있는지 확인
    n = len(relation)   # 자료개수
    m = len(relation[0])    # 컬럼 개수
    arr = [0] * m
    result = []
    choice(0)
    print(result)
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)


# google에서 찾은 정답
from itertools import combinations
def solution2(relation):
    n = len(relation)
    m = len(relation[0])
    candidates = []
    for i in range(1,m+1):
        candidates.extend(combinations(range(m),i))
    # print(candidates)
    unique = []
    for candi in candidates:
        tmp = [tuple([item[i] for i in candi]) for item in relation]
        # print(tmp)
        if len(set(tmp)) == n:
            unique.append(candi)
    print(unique)
    
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])
    print(answer)    
    return len(answer)
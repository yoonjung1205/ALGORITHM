def solution(citations):
    answer = 0

    # 한편의 논문도 인용되지 못한 경우 처리
    if max(citations) == 0:
        return 0

    # citations.sort()
    h = 1
    while h <= max(citations):
        quote = 0
        for i in range(len(citations)):
            if h <= citations[i]:
                quote += 1
        if quote >= h:
            answer = h

        h += 1

    return answer
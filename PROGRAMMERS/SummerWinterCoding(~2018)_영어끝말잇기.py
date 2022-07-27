def solution(n, words):
    answer = []
    temp = []
    for i in range(len(words)):
        if words[i] in temp:
            answer.append((i % n) + 1)  # 번호
            answer.append((i // n) + 1)  # 차례
            break
        if i != 0 and words[i][0] != words[i - 1][-1]:
            answer.append((i % n) + 1)  # 번호
            answer.append((i // n) + 1)  # 차례
            break
        temp.append(words[i])
    if not answer:
        answer = [0, 0]

    return answer
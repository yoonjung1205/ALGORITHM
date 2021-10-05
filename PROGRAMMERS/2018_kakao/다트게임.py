def solution(dartResult):
    option = '*#'
    score = [0] * 3
    print(score)
    idx = -1
    for i in range(len(dartResult)):
        if dartResult[i].isdecimal():
            idx += 1
            if dartResult[i] == '0':
                continue
            if i != len(dartResult) - 1:
                if dartResult[i + 1].isdecimal():
                    score[idx] = 10
                    idx -= 1

                else:
                    score[idx] = int(dartResult[i])

        # 보너스 처리
        elif dartResult[i].isalpha():
            if dartResult[i] == 'S':
                score[idx] **= 1

            elif dartResult[i] == 'D':
                score[idx] **= 2
            else:
                score[idx] **= 3
        # 옵션
        elif dartResult[i] in option:
            if dartResult[i] == '*':
                if idx == 0:
                    score[idx] *= 2
                else:
                    score[idx - 1] *= 2
                    score[idx] *= 2
            else:
                score[idx] *= -1

    answer = sum(score)
    return answer
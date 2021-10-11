def solution(msg):
    answer = []
    alpha = {}
    # print(chr(65))
    # 'A':1,'B':2,...,'Z':26 딕셔너리에 저장
    for i in range(26):
        alpha[chr(65 + i)] = i + 1

    # 새로만들 key값 변경을 위한 cnt 설정
    cnt = 1

    # i = 기준, j = 변경
    i = 0
    while i < len(msg):
        j = len(msg)
        while msg[i:j] not in alpha:  # 문자열이 딕셔너리안에 있을 때 까지 j 줄이자
            j -= 1

        answer.append(alpha[msg[i:j]])  # 이까지 왔으면, 문자열(i~j-1)이 딕셔너리 안에 있을 테니까, answer에 더해줌
        if j == len(msg):  # j가 처음값과 같으면, 문자열 끝까지 다본것(다음문자가 없음)이므로 반복문 종료
            break
        alpha[msg[i:j + 1]] = 26 + cnt  # 딕셔너리에 다음문자까지 해서 등록한다.
        cnt += 1
        if len(msg[i:j + 1]) > 2:  # 문자열의 길이가 2보다 크면 다음에 봐야할 문자도 그만큼 크게 해준다.
            i += len(msg[i:j + 1]) - 1
        else:
            i += 1

    # print(alpha)
    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))
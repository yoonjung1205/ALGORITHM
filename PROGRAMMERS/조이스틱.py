def solution(name):
    answer = 0

    def up_down(ch):
        up = abs(65 - ord(ch))
        down = abs(90 - ord(ch) + 1)
        return min(up, down)

    index = 0
    min_move = len(name) - 1

    while index < len(name):
        answer += up_down(name[index])
        start = index + 1
        # 연속된 A의 마지막 인덱스 start
        while start < len(name) and name[start] == 'A':
            start += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * index + len(name) - start, index + 2 * (len(name) - start)])
        index += 1
    answer += min_move

    return answer
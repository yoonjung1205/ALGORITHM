# imos법 사용
# 참고 (https://driip.me/65d9b58c-bf02-44bf-8fba-54d394ed21e0)

def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    temp = [[0] * (m + 1) for _ in range(n + 1)]

    # print(temp)
    for kind, r1, c1, r2, c2, degree in skill:
        # 공격
        if kind == 1:
            temp[r1][c1] -= degree
            temp[r1][c2 + 1] += degree
            temp[r2 + 1][c1] += degree
            temp[r2 + 1][c2 + 1] -= degree
        # 회복
        else:
            temp[r1][c1] += degree
            temp[r1][c2 + 1] -= degree
            temp[r2 + 1][c1] -= degree
            temp[r2 + 1][c2 + 1] += degree

    # 행 누적합
    for i in range(n + 1):
        for j in range(1, m + 1):
            temp[i][j] += temp[i][j - 1]
    # 열 누적합
    for j in range(m + 1):
        for i in range(1, n + 1):
            temp[i][j] += temp[i - 1][j]

    for i in range(n):
        for j in range(m):
            if board[i][j] + temp[i][j] > 0:
                answer += 1
    return answer
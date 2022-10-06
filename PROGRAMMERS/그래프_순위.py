# 전형적인 플로이드 와샬 문제!!

def solution(n, results):
    answer = 0
    arr = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(len(results)):
        arr[results[i][0]][results[i][1]] = 1
        arr[results[i][1]][results[i][0]] = -1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if arr[i][j] == 0:
                    if arr[i][k] == 1 and arr[k][j] == 1:
                        arr[i][j] = 1
                    elif arr[i][k] == -1 and arr[k][j] == -1:
                        arr[i][j] = -1

    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            #     print(arr[i][j], end=" ")
            # print()
            if i == j:
                continue
            elif arr[i][j] == 0:
                break
            else:
                cnt += 1
                if cnt == n - 1:
                    answer += 1
    return answer
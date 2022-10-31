from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    result = [-2] * (n + 1)
    arr = [[] for _ in range(n + 1)]
    for r in roads:
        arr[r[0]].append(r[1])
        arr[r[1]].append(r[0])

    def bfs(start, count):
        q = deque()
        q.append([start, count])
        visit[start] = 1

        while q:
            now, cnt = q.popleft()
            for t in arr[now]:
                if not visit[t]:
                    if t in sources:
                        result[t] = cnt + 1
                    visit[t] = 1
                    q.append([t, cnt + 1])

    visit = [0] * (n + 1)
    bfs(destination, 0)
    for s in sources:
        # 출발지 = 목적지
        if s == destination:
            answer.append(0)

        # 이동하지 못하는 경우
        elif result[s] == -2:
            answer.append(-1)

        else:
            answer.append(result[s])

    return answer
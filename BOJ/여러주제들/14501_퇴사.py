from collections import deque
N = int(input())
info = []
info.append([])
for _ in range(N):
    info.append(list(map(int,input().split())))

# print(info)

final_total = 0


def bfs(start,total):
    global final_total
    q = deque()
    q.append([start, total])

    while q:
        a, t = q.popleft()
        for i in range(a+info[a][0],N+1):
            if i + info[i][0] <= N + 1:
                q.append([i, t+info[i][1]])

        if t >= final_total:
            final_total = t


for i in range(1, N+1):
    total = 0
    if i + info[i][0] > N + 1:
        continue

    bfs(i,info[i][1])


print(final_total)


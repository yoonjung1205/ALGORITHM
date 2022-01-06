# 어느도시에서 출발하더라도 똑같아서 for문으로 bfs안해줘도 된다.


N = int(input())

adj = [list(map(int,input().split())) for _ in range(N)]
visited = [0] * N
# print(adj)

def bfs(cur, tot, start):
    global ans
    if cur == N:
        if adj[cur][start] != 0:
            if tot < ans:
                ans = tot
            return
    if tot > ans:
        return
    for i in range(N):
        if visited[i] and adj[cur][i] == 0:
            continue

        visited[i] = 1
        bfs(cur+1, tot+adj[cur][i], start)
        visited[i] = 0

ans = 987654321

for i in range(N):
    bfs(0,0,i)

print(ans)
from collections import deque

def bfs(s):
    q = deque()
    visited[s] = 1
    q.append(s)
    while q:
        t = q.popleft()

        for i in range(1,N+1):
            if arr[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1



a, b = map(int,input().split())
N, M = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    v1,v2 = map(int,input().split())
    arr[v1][v2] = 1
    arr[v2][v1] = 1

visited = [0] * (N+1)
bfs(a)

if visited[b]:
    print(visited[b]-1)
else:
    print(-1)


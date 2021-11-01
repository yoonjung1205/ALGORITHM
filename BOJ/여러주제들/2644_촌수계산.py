# from pprint import pprint

def bfs(v):
    q = []
    visited[v] = 1
    q.append(v)
    while q:
        t = q.pop(0)
        for i in range(n+1):
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

# 전체 사람 수
n = int(input())
s,e = map(int,input().split())
m = int(input())
adj = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    p,c = map(int,input().split())
    adj[p][c] = 1
    adj[c][p] = 1

# pprint(adj)

visited = [0]*(n+1)

bfs(s)
if visited[e]-1:
    print(visited[e]-1)
else:
    print(-1)
def dfs(v):
    visit[v] = 1
    print(v,end=' ')
    for i in adj_arr[v]:
        if not visit[i]:
            dfs(i)

def bfs(v):
    q = []
    visit[v] = 1
    q.append(v)
    
    while q:
        t = q.pop(0)
        print(t,end=' ')
        for i in adj_arr[t]:
            if not visit[i]:
                q.append(i)
                visit[i] = 1


# n: 정점 개수, m: 간선 개수, v: 시작점
n, m, v = map(int,input().split())
adj_arr = [[] for _ in range(n+1)]

for i in range(m):
    s,e = map(int,input().split())
    adj_arr[s].append(e)
    adj_arr[e].append(s)
    
for i in range(n+1):
    adj_arr[i].sort()
# print(adj_arr)



visit = [0]*(n+1)

dfs(v)
print()
visit = [0]*(n+1)
bfs(v)
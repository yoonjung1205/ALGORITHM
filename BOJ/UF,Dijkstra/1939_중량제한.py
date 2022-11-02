from collections import deque

N, M = map(int,input().split())
arr = []
for _ in range(M):
    a,b,w = map(int, input().split())
    arr.append([a,b,w])

# 최대신장트리를 만들어서 bfs로 목표지점까지 가중치 가장 작은 값 찾기
par = list(range(N+1))

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(x,y):
    x = find(x)
    y = find(y)
    par[x] = y
    return

arr.sort(key=lambda x:x[2], reverse=True)
# print(arr)
arr2 = [[] for _ in range(N+1)]
for i in range(len(arr)):
    x = arr[i][0]
    y = arr[i][1]
    w = arr[i][2]
    if find(x) == find(y):
        continue
    arr2[x].append([y,w])
    arr2[y].append([x, w])
    union(x,y)

# print(arr2)

s, e = map(int,input().split())
visit = [0] * (N+1)

def bfs(start,weight):
    q = deque()
    q.append([start,weight])
    visit[start] = 1

    while q:
        now, m = q.popleft()
        if now == e:
            print(m)
            return
        for t in arr2[now]:
            if not visit[t[0]]:
                q.append([t[0],min(m,t[1])])
                visit[t[0]] = 1

bfs(s,1000000001)





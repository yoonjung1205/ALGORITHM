import heapq

def dijkstra(X):
    q = []
    heapq.heappush(q,[0,X])
    d[X] = 0

    while q:
        dist, now = heapq.heappop(q)
        for t in arr[now]:
            c = dist + t[1]
            if c < d[t[0]]:
                d[t[0]] = c
                heapq.heappush(q,[c,t[0]])


# N: 학생 수, M: 간선 수, X: 파티장소
N,M,X = map(int, input().split())

arr = [[] for _ in range(N+1)]
for i in range(M):
    s,e,w = map(int,input().split())
    arr[s].append([e,w])
INF = 987654321
d = [INF] * (N+1)
dijkstra(X)
X_to_Node = d[::]
# print(X_to_Node)
for i in range(1,N+1):
    if i == X:
        continue
    d = [INF] * (N+1)
    dijkstra(i)
    X_to_Node[i] = X_to_Node[i] + d[X]
X_to_Node.pop(0)
print(max(X_to_Node))

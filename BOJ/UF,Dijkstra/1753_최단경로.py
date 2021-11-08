import heapq
import sys

def dijkstra(start):
    q = []
    heapq.heappush(q,[0,start]) # q, [가중치,시작점]
    d[start] = 0

    while q:
        distance, now = heapq.heappop(q)
        if d[now] < distance:
            continue
        for i in arr[now]:
            c = distance + i[1]
            if c < d[i[0]]:
                d[i[0]] = c
                heapq.heappush(q,[c,i[0]])
                

input = sys.stdin.readline
V,E = map(int,input().split())
start = int(input())
arr = [[] for _ in range(V+1)]

for i in range(E):
    s,e,w = map(int,input().split())
    arr[s].append([e,w])

# print(arr)
INF = 987654321
d = [INF] * (V+1)
dijkstra(start)

for i in range(1,V+1):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])
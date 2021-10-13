def search(n):
    visited[n] = 1
    for i in edge[n]:
        if not visited[i]:
            search(i)

V = int(input())
E = int(input())

edge = [[]*(V+1) for _ in range(V+1)]

# 인접리스트 만들기
for i in range(E):
    n1,n2 = map(int,input().split())
    edge[n1].append(n2)
    edge[n2].append(n1)

# print(edge)
visited = [0] * (V+1)

search(1)
print(sum(visited)-1)
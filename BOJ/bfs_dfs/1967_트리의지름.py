def dfs(s,d):
    global length

    for i in tree[s]:
        if not visited[i[0]]:
            visited[i[0]] += d+i[1] # d = 거리 누적값
            dfs(i[0],d+i[1])



n = int(input())

tree = [[]*(n+1) for _ in range(n+1)]
for i in range(n-1):
    a, b, w = map(int, input().split())
    tree[a].append([b, w])
    tree[b].append([a, w])

visited = [0]*(n+1)
ans = 0
length = 0
visited[1] = 1
dfs(1,0)


# print(visited)
for i in range(len(visited)):
    if visited[i] == max(visited):
        idx = i
        break
visited = [0]*(n+1)
dfs(idx,0)
# print(visited)

print(max(visited))

'''
5
1 2 3
1 3 4
1 4 5
1 5 6
'''
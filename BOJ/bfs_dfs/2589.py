from collections import deque

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def bfs(x,y):
    global result
    visit = [[0]*m for _ in range(n)]
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc] and map[nr][nc]=='L':
                q.append([nr,nc])
                visit[nr][nc] = visit[r][c] + 1
        ans = visit[r][c]
        if result < ans:
            result = ans

n,m = map(int,input().split())

map = [list(input()) for _ in range(n)]

result = 0

# print(map)

for i in range(n):
    for j in range(m):
        if map[i][j]=='L':
            bfs(i,j)

print(result-1)
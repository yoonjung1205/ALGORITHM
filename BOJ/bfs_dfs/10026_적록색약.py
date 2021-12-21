from collections import deque

N = int(input())

color = [list(input()) for _ in range(N)]

# print(color)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(r,c):
    q = deque()
    q.append([r,c])
    visited[r][c] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if color[x][y] == color[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = 1



visited = [[0]*N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt += 1
            bfs(i,j)

for i in range(N):
    for j in range(N):
        if color[i][j] == 'G':
            color[i][j] = 'R'

visited = [[0]*N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt2 += 1
            bfs(i,j)

print(cnt, cnt2)
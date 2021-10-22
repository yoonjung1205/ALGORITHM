from collections import deque

dr=[-1,0,1,0]
dc=[0,1,0,-1]
def bfs(x,y):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc] and miro[nr][nc]==1:
                q.append([nr,nc])
                visit[nr][nc] = visit[r][c] + 1


n,m = map(int,input().split())
miro = [list(map(int,input())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
# print(miro)
bfs(0,0)
# print(visit)
print(visit[n-1][m-1])

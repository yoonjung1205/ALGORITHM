'''
3차원visit 사용
visit[x][y][wall] 에 visit 기록하고
wall = 0이면 벽 안부순 경로, wall = 1 이면 벽 부순 경로
'''
from collections import deque

N, M = map(int,input().split())
mmap = [list(map(int,input())) for _ in range(N)]

visit = [[[0]*2 for _ in range(M)]for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 일반버전(pypy가 더빠름)
q = deque()
q.append([0,0,0])
visit[0][0][0] = 1

while q:
    x,y,wall = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0<=ny<M and visit[nx][ny][wall]==0:
            if mmap[nx][ny] == 0:
                q.append([nx, ny, wall])
                visit[nx][ny][wall] = visit[x][y][wall] + 1
            if mmap[nx][ny] == 1 and wall==0:
                q.append([nx,ny,1])
                visit[nx][ny][1] = visit[x][y][wall] + 1

if max(visit[N-1][M-1]) == 0:
    print(-1)
elif visit[N-1][M-1][0] != 0 and visit[N-1][M-1][1] != 0:
    print(min(visit[N-1][M-1]))
else:
    print(max(visit[N-1][M-1]))


# 함수버전
def bfs():
    q = deque()
    q.append([0,0,0])
    visit[0][0][0] = 1

    while q:
        x,y,wall = q.popleft()  #wall == 0 이면 벽부수지 않은 경로
        if  x == N-1 and y == M-1:
            return visit[x][y][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0<=ny<M  and visit[nx][ny][wall]==0:
                if mmap[nx][ny] == 0:
                    q.append([nx, ny, wall])
                    visit[nx][ny][wall] = visit[x][y][wall] + 1
                if mmap[nx][ny] == 1 and wall==0:
                    q.append([nx,ny,1])
                    visit[nx][ny][1] = visit[x][y][wall] + 1

    return -1

print(bfs())
from collections import deque

N, M = map(int, input().split())
miro = []
for _ in range(N):
    miro.append(list(input()))
visit = [[[0]*64 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = deque()
for i in range(N):
    for j in range(M):
        if miro[i][j] == '0':
            q.append([i,j,0])
            miro[i][j] = '.'
            visit[i][j][0] = 1
flag = 0
while q:
    x,y,key = q.popleft()
    if miro[x][y] == '1':
        flag = 1
        print(visit[x][y][key]-1)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M and visit[nx][ny][key] == 0 and miro[nx][ny] != '#':
            if miro[nx][ny] in 'abcdef':
                # nkey = ord(miro[nx][ny].upper())-64
                nkey = key | (1 << (ord(miro[nx][ny].upper()) - 65))
                if visit[nx][ny][nkey] == 0:
                    q.append([nx, ny, nkey])
                    visit[nx][ny][nkey] = visit[x][y][key] + 1
            elif miro[nx][ny] in 'ABCDEF':
                if key & (1 << (ord(miro[nx][ny].upper()) - 65)):
                    q.append([nx,ny,key])
                    visit[nx][ny][key] = visit[x][y][key] + 1
                else:
                    continue
            else:
                q.append([nx, ny,key])
                visit[nx][ny][key] = visit[x][y][key] + 1

if flag == 0:
    print(-1)


'''
4 5
#f#..
#.#..
#a#..
0.FA1
'''
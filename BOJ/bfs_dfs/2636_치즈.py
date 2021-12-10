from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]


# 절대생각못할듯...ㅠㅠ
def bfs():
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if cheese[nx][ny] == 0:
                    q.append([nx,ny])
                    visited[nx][ny] = 1

                else:
                    visited[nx][ny] = 1
                    cheese[nx][ny] = 0
                    cnt += 1
    cnt_list.append(cnt)
    return cnt


R, C = map(int, input().split())
cheese = [list(map(int,input().split())) for _ in range(R)]


cnt_list = []

cycle = 0
while 1:
    cycle += 1
    visited = [[0] * C for _ in range(R)]
    cheese_cnt = bfs()
    if cheese_cnt == 0:
        break

print(cycle-1)
print(cnt_list[-2])
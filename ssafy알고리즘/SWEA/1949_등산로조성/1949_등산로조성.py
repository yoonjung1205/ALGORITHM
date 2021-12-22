import sys
sys.stdin = open('input.txt')

T = int(input())


'''dx = [-1,0,1,0] # 상,우,하,좌
dy = [0,1,0,-1]

def dfs(x,y):
    global cnt
    if not visited[x][y]:
        visited[x][y] = 1


    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if map_info[x][y] > map_info[nx][ny]:
                cnt += 1
                dfs(nx, ny)
                # visited[nx][ny] = 0
            # elif map_info[nx][ny] - 1:'''

# 1. 현재 위치를 들고다니지 않을 때
# r,c 좌표, road: 등산로길이 ,skill: 공사 유무
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def work(r,c,road,skill):
    global ans
    if road > ans: ans = road

    visited[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # 현위치보다 낮은 곳으로 이동할 때
            if map_info[r][c] > map_info[nr][nc]:
                work(nr,nc,road+1,skill)
            # 현위치보다 높거나 같은 곳으로 이동할 때
            elif skill and map_info[r][c] > map_info[nr][nc] - K:
                tmp = map_info[nr][nc]
                map_info[nr][nc] = map_info[r][c] - 1
                work(nr,nc,road+1,0)
                map_info[nr][nc] = tmp

    visited[r][c] = 0

# 2. 현재 위치를 들고다니자..
def work2(r,c,h,road,skill):
    global ans
    if road > ans: ans = road
    visited[r][c] = 1
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]: continue

        if h > map_info[nr][nc]:
            work2(nr,nc,map_info[nr][nc], road+1, skill)
        elif skill and h>map_info[nr][nc]-K:
            work2(nr, nc, map_info[r][c]-1, road + 1, 0)
    visited[r][c] = 0

for tc in range(1,T+1):
    # N: 한변의 길이, K: 최대 공사가 가능한 깊이
    N,K = map(int,input().split())
    # map_info = [list(map(int,input().split())) for _ in range(N)]
    #
    # # 최고 봉우리 값 구하기
    # max_p = 0
    # for i in range(N):
    #     if max_p < max(map_info[i]):
    #         max_p = max(map_info[i])

    map_info = []
    max_p = 0
    for i in range(N):
        # 한 줄 입력을 받고 내부에서 가장 큰 값을 찾자
        tmp = list(map(int,input().split()))

        for j in tmp:
            if max_p < j:
                max_p = j
        map_info.append(tmp)

    # # 봉우리 좌표 저장
    # v = []
    # for i in range(N):
    #     for j in range(N):
    #         if map_info[i][j] == max_p:
    #             v.append([i,j])

    visited = [[0]*N for _ in range(N)]

    # 등산로 길이
    ans = 0
    for i in range(N):
        for j in range(N):
            if map_info[i][j] == max_p:
                work(i,j,1,1)
                work2(i,j,max_p,1,1)


    print('#{} {}'.format(tc,ans))
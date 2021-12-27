import heapq

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dijkstra():
    q = []
    heapq.heappush(q,[cave[0][0],0,0])
    visited[0][0] = cave[0][0]
    while q:
        d,x,y = heapq.heappop(q)
        if x == N-1 and y == N-1:
            return d

        # if d > visited[x][y]:
        #     continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                nd = cave[nx][ny] + d
                if visited[nx][ny] > nd:
                    visited[nx][ny] = nd
                    heapq.heappush(q,[nd,nx,ny])

cnt = 1
while True:
    N = int(input())
    if N == 0:
        quit()

    cave = [list(map(int, input().split())) for _ in range(N)]
    visited = [[9999]*N for _ in range(N)]

    ans = dijkstra()
    print('Problem {}: {}'.format(cnt,ans))
    cnt += 1
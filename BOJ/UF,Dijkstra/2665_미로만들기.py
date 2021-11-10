import heapq

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dijkstra(r,c):
    global ans
    q = []
    heapq.heappush(q,[0,r,c])
    d[0][0] = 0
    while q:
        dist,x,y = heapq.heappop(q)
        if x == N-1 and y == N-1:
            return

        if dist > d[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if miro[nx][ny] == 0:
                    n_dist = dist + miro[nx][ny] + 1    
                else:
                    n_dist = dist + miro[nx][ny] -1
                if n_dist < d[nx][ny]:
                    d[nx][ny] = n_dist
                    heapq.heappush(q,[n_dist,nx,ny])

N = int(input())
miro = [list(map(int,input())) for _ in range(N)]
# print(miro)
INF = 987654321
d = [[INF] * N for _ in range(N)]
# print(d)
ans = 0
dijkstra(0,0)
print(d[N-1][N-1])
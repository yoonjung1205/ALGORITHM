c,r = map(int,input().split())
k = int(input())

arr = [[0]*(r) for _ in range(c)]

dx = [0,1,0,-1]#우,하,좌,상
dy = [1,0,-1,0]
num = 1
x = 0
y = -1
i = 0

if k > r*c:
    print(0)
    exit()
while num <= k:
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < c and ny < r and arr[nx][ny] == 0:
        arr[nx][ny] = num
        num += 1
        x = nx
        y = ny
    else:
        i = (i+1) % 4

print(nx+1,ny+1)

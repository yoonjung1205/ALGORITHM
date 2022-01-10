dx = [0,1,0,-1]
dy = [1,0,-1,0]

# print(ord('Z')) # 65 ~ 90


def dfs(x,y,cnt):
    global ans
    if ans < cnt:
        ans = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(arr[nx][ny])]:
            visited[ord(arr[nx][ny])] = 1
            dfs(nx,ny,cnt+1)
            visited[ord(arr[nx][ny])] = 0


R, C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
visited = [0] * 100
# print(arr)
ans = 0
visited[ord(arr[0][0])] = 1
dfs(0,0,1)
print(ans)


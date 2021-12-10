# 조금 더 빠름
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(r,c):
    global cnt,house
    
    visit[r][c] = cnt
    count[r][c] = house
    s = []
    s.append([r,c])
    while s:
        x,y = s.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and apart[nx][ny] == 1:
                house += 1
                s.append([nx,ny])
                visit[nx][ny] = cnt
                count[nx][ny] = house
                

N = int(input())
apart = [list(map(int,input())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
count = [[0]*N for _ in range(N)]
cnt = 0
result = []

for i in range(N):
    for j in range(N):
        if apart[i][j] == 1 and visit[i][j] == 0:
            house = 1
            cnt += 1
            dfs(i,j)
            result.append(house)

print(cnt)
result.sort()
for i in range(len(result)):
    print(result[i])


####################################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(r,c):
    global cnt
    
    visit[r][c] = cnt
    s = []
    s.append([r,c])
    while s:
        x,y = s.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and apart[nx][ny] == 1:
                s.append([nx,ny])
                visit[nx][ny] = cnt
                
                

N = int(input())
apart = [list(map(int,input())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
cnt = 0

result = []

# print(visit)
# print(apart)

for i in range(N):
    for j in range(N):
        if apart[i][j] == 1 and visit[i][j] == 0:
            cnt += 1
            dfs(i,j)

result = [0] * (cnt+1)

for i in range(N):
    for j in range(N):
        for k in range(len(result)):
            if k != 0 and visit[i][j] == k:
                result[k] += 1

# print(result)
print(cnt)
result.sort()
for i in range(1,len(result)):
    print(result[i])




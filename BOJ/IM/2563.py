N = int(input())
r = [list(map(int,input().split())) for _ in range(N)]

arr =[[0]*101 for _ in range(101)]

area = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            continue
        for k in range(N):
            if r[k][0]<= i < r[k][0]+10 and r[k][1]<= j < r[k][1]+10:
                arr[i][j] = 1
                
                
for i in range(101):
    for j in range(101):
        if arr[i][j]==1:
            area += 1
    
print(area)
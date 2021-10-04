r = [list(map(int,input().split())) for _ in range(4)]

arr =[[0]*101 for _ in range(101)]

area = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            continue
        for k in range(4):
            if r[k][0]<= i < r[k][2] and r[k][1]<= j < r[k][3]:
                arr[i][j] = 1
                
                
for i in range(101):
    for j in range(101):
        if arr[i][j]==1:
            area += 1
    
print(area)
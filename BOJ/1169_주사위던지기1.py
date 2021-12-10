n,m = map(int,input().split())

def dice1(cur):
    if cur == n:
        print(*arr)
        return
    
    for i in range(6):
        arr[cur] = i+1
        dice1(cur+1)

def dice2(cur,start):
    if cur == n:
        print(*arr)
        return

    for i in range(start,7):
        arr[cur] = i
        dice2(cur+1,i)

def dice3(cur):
    if cur == n:
        print(*arr)
        return

    for i in range(6):
        if visit[i]:
            continue
        visit[i] = 1
        arr[cur] = i+1
        dice3(cur+1)
        visit[i] = 0

        
arr = [0]*n
visit = [0]*6
if m == 1:
    dice1(0)

if m == 2:
    dice2(0,1)

if m == 3:
    dice3(0)


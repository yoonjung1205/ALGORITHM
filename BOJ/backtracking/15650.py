m,n = map(int,input().split())
arr = [0]*n

def recur(cur,start):
    if cur == n:
        print(*arr)
        return

    for i in range(start,m):
        arr[cur] = i+1
        recur(cur+1,i+1)

recur(0,0)
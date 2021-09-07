m,n=map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
a = [0]*n
def recur(cur,start):
    if cur == n:
        print(*a)
        return
    
    for i in range(start,m):
        a[cur]=arr[i]
        recur(cur+1,i+1)

recur(0,0)
    
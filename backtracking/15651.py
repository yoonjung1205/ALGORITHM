m,n = map(int,input().split())
arr = [0] * n
def recur(cur):
    if cur == n:
        print(*arr)
        return
    for i in range(m):
        arr[cur] = i+1
        recur(cur+1)

recur(0)
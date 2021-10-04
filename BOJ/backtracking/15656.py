m,n = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

a = [0]*n
def recur(cur):
    if cur == n:
        print(*a)
        return

    for i in range(m):
        a[cur]=arr[i]
        recur(cur+1)

recur(0)
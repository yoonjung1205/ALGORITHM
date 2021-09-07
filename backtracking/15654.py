m, n = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

a = [0]*n
visited=[0]*m
def recur(cur):
    if cur == n:
        print(*a)
        return

    for i in range(m):
        if visited[i]:
            continue

        visited[i] = 1
        a[cur] = arr[i]
        recur(cur+1)
        visited[i] = 0


recur(0)
m,n = map(int,input().split())
arr = [0]*n

visited = [0] * (m+1)
def recur(cur):
    if cur == n:
        print(*arr)
        return
    
    for i in range(1,m+1):
        if visited[i]:
            continue
        visited[i] = 1
        arr[cur] = i
        recur(cur+1)
        visited[i] = 0    
recur(0)
        
a,b = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
tmp = []
visit = [0]*a

def recur(cur):
    if cur == b:
        print(*tmp)
        return
    check = 0

    for i in range(a):
        if not visit[i] and check != arr[i]:
            tmp.append(arr[i])
            visit[i] = 1
            check = arr[i]
            recur(cur+1)
            tmp.pop()
            visit[i] = 0

recur(0)
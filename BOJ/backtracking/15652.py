n = 2
m = 4
arr = [0] * n

def recur(cur, start):
    if cur == n:
        print(*arr)
        return

    for i in range(start, m):
        arr[cur] = i+1
        recur(cur + 1, i)

recur(0, 0)
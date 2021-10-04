d = []
for i in range(9):
    d.append(int(input()))
n=7
m=9

arr = []

def recur(cur, cnt):
    if cnt == n:
        if sum(arr)==100:
            arr.sort()
            for i in range(n):
                print(arr[i])
            return
        return
    if cur == m + 1:
        return

    arr.append(d[cur-1])
    recur(cur + 1, cnt + 1)
    arr.pop()
    recur(cur + 1, cnt)

recur(1, 0)
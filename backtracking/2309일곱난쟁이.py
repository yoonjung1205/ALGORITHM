d = []
for i in range(9):
    d.append(int(input()))
n=7
m=9

arr = []
def recur(cur,cnt,total):
    if cnt == n and total == 100:
        for i in range(n):
            print(arr[i])
        return

    if cur == m+1 or total > 100:
        return

    arr.append(d[cnt])
    recur(cur+1,cnt+1,sum(arr))
    arr.pop()
    recur(cur+1,cnt,sum(arr))

recur(1,0,0)
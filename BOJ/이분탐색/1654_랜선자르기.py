K, N = map(int, input().split())

arr = []
for i in range(K):
    arr.append(int(input()))

arr.sort()
print(arr)

s = 1
e = 1000000

def check(x):
    p = arr[0]
    cnt = 1

    for i in range(1, K):
        if arr[i] >= p + x:
            cnt += 1
            p = arr[i]

    return cnt >= N

while s <= e:
    mid = (s+e)//2

    if mid :
        ans = mid
        s = mid + 1

    else:
        e = mid - 1

print(ans)
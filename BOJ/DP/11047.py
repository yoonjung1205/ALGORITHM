N ,K = map(int,input().split())

arr = [int(input()) for _ in range(N)]
arr = sorted(arr,reverse=True)
cnt = 0
ans = 0
for i in range(N):
    if arr[i] <= K:
        while K >= arr[i]:
            cnt = K // arr[i] 
            K %= arr[i]
        ans += cnt
    if K == 0:
        break

print(ans)
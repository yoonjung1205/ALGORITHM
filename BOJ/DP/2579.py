n = int(input())
arr = [0]+[int(input()) for _ in range(n)]
dp = [0] * len(arr)

if n==1:
    print(arr[1])
    exit()


dp[1] = arr[1]
dp[2] = arr[1]+arr[2]
if n==2:
    print(dp[2])
    exit()

dp[3] = max(arr[2]+arr[3],arr[1]+arr[3])

for i in range(4,len(arr)):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])

print(dp[n])
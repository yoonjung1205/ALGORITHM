n = int(input())
arr = [0]+list(map(int,input().split()))

dp = [987654321]*len(arr)
dp[1] = arr[1]
# n이 1인 경우
if n == 1:
    print(arr[1])
    exit()
cur_sum = arr[1] + arr[2]
# 음수일 경우
if arr[1]<0 and arr[1]<arr[2]:
    cur_sum = arr[2]
dp[2] = max(dp[1],cur_sum)
ans = dp[2]

for i in range(3,n+1):
    cur_sum = max(arr[i], cur_sum+arr[i])
    ans = max(cur_sum,ans)
    dp[i] = ans

print(dp[n])

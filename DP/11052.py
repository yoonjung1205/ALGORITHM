N = int(input())

cost = [0] + list(map(int,input().split()))

dp = [0 for _ in range(1001)]
dp[1] = cost[1]
dp[2] = max(cost[1]*2,cost[2])
dp[3] = max(dp[2],cost[3])

for i in range(3,N+1):
    

for i in range(N+1):
    print(dp[i])

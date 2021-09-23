n = int(input())
'''table = [-1] * 1001

def dp(n):
    if table[n] != -1:
        return table[n]

    if n == 1:
        table[n] = 1
        return table[n]
    if n == 2:
        table[n] = 3
        return table[n]
    else:
        table[n] = dp(n-1) + 2*dp(n-2)
        return table[n]%10007

print(dp(n))'''

dp = [-1] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3,n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[n]%10007)
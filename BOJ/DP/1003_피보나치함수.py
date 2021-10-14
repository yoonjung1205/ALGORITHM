T = int(input())

for tc in range(T):
    n = int(input())
    dp = [0] * 100
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    ans = [0,0] * 100


    # n의 0과 1의 호출 횟수는 0: 피보나치 n-1의 수,1: 피보나치 n의 수와 같다.
    ans[0] = [1,0]
    ans[1] = [0,1]
    for i in range(2,n+1):
        ans[i] = [dp[i-1],dp[i]]

    print(*ans[n])

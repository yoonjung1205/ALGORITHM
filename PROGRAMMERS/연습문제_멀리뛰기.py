def solution(n):
    answer = 0

    dp = [0] * 1234567
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(3, 2001):
        dp[i] = dp[i - 2] + dp[i - 1]
    answer = dp[n] % 1234567

    return answer
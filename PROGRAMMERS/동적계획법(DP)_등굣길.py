def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[1][1] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i == 1 and j == 1:
                continue
            if [i,j] in puddles:
                dp[i][j] = 0
                
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
            
            
            
    answer = dp[m][n]
    return answer

# def solution(m,n,puddles):
#     dp = [[0]*(n+1) for _ in range(m+1)]
#     dp[1][1] = 1
#     for k in range(len(puddles)):
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 if i == 1 and j == 1:
#                     continue
#                 if i==puddles[k][0] and j==puddles[k][1]:
#                     dp[i][j] = 0
#                 else:
#                     dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
#     print(dp[m][n])
#     return dp[m][n]
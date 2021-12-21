arr = list(input())
arr2 = list(input())
dp = [[0]*(len(arr2)+1) for _ in range(len(arr)+1)]

for i in range(1,len(arr)+1):
    for j in range(1,len(arr2)+1):
        if arr[i-1] == arr2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

# for i in range(len(arr)+1):
#     for j in range(len(arr2)+1):
#         print(dp[i][j], end=" ")
#     print()

print(dp[-1][-1])




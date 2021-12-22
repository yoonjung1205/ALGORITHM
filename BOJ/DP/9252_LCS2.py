arr = list(input())
arr2 = list(input())
dp = [['']*(len(arr2)+1) for _ in range(len(arr)+1)]

# 잘모르겠어서 구선생 도움을 받음.. (dp에 숫자대신 입력받은 문자열을 직접 넣어줌)
for i in range(1,len(arr)+1):
    for j in range(1,len(arr2)+1):
        if arr[i-1] == arr2[j-1]:
            dp[i][j] = dp[i-1][j-1] + arr[i-1]

        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[-1][-1]))
if len(dp[-1][-1]) == 0:
    quit()
print(dp[-1][-1])




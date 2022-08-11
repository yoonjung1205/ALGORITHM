import sys
input = sys.stdin.readline

N ,M = map(int,input().split())

arr = [[0]+list(map(int,input().split())) for _ in range(N)]
arr.insert(0,[0]*(M+1))

# 누적합 계산
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]


# 부분행렬 다돌기
'''
A | B | C
ㅡㅡㅡㅡㅡ
D | E | F
ㅡㅡㅡㅡㅡ
G | H | I

부분행렬 안에 있는 정수들의 합을 구하는 것도 누적합을 구하는 것과 비슷하다.
위의 그림에서 (E+F+H+I)를 구하고 싶으면 I까지의 누적합(A+B+C+...+H+I)에서
C까지의 누적합(A+B+C)과 G까지의 누적합(A+D+G)을 빼 준 뒤
겹치는 부분인 A를 더해주면 된다.
출처 (https://hbj0209.tistory.com/142)
'''
answer = -4000001
for x1 in range(1,N+1):
    for y1 in range(1,M+1):
        for x2 in range(x1,N+1):
            for y2 in range(y1,M+1):
                # print(x1,y1,x2,y2)
                # print(dp[x2][y2] - dp[x2][y1] - dp[x1][y2] + dp[x1][y1])

                if answer <= dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]:
                    answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]

print(answer)
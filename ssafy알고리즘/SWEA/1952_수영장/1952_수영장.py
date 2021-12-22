import sys
sys.stdin = open('input.txt')

T = int(input())

# cost 이전 달 까지의 계산결과, m 현재 내가 보낼 결과
'''def calc(cost,m):
    global min_cost
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return

    # # 1일권
    # calc(cost + d*month[m], m + 1)
    # # 1달권
    # calc(cost + m1, m + 1)
    # 1일,1달
    calc(cost + min(d*month[m],m1),m+1)
    # 3달권
    calc(cost + m3, m + 3)

for tc in range(1,T+1):
    d, m1,m3,y = map(int,input().split())

    month = [0] + list(map(int, input().split()))

    min_cost = y # 1년치 비용이 현재 최저의 가격
    calc(0,1)
    
    print('#{} {}'.format(tc,min_cost))'''


########################################################
for tc in range(1,T+1):
    d, m1,m3,y = map(int,input().split())

    month = [0] + list(map(int, input().split()))

    dp = [0] * 13
    dp[1] = min(m1,month[1]*d)
    dp[2] = dp[1] + min(m1,month[2]*d)

    for i in range(3,13):
        dp[i] = min(dp[i-3]+m3, dp[i-1]+m1, dp[i-1]+month[i]*d)

    print('#{} {}'.format(tc,min(dp[12],y)))
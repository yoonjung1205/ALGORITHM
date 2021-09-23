import sys

N,M = map(int,sys.stdin.readline().split())
my_list = [0] + list(map(int,sys.stdin.readline().split()))


'''
l = len(my_list)
for i in range(M):
    s,e = map(int,input().split())
    ans1 = 0
    ans2 = 0
    for i in range(l):
        if i <= e:
            ans1 += my_list[i]
        if i <= s-1:
            ans2 += my_list[i]
    print(ans1-ans2)'''

dp = [0 for _ in range(100001)]
dp[1] = my_list[1]
for i in range(2,len(my_list)):    
    dp[i] = dp[i-1]+my_list[i]

for i in range(M):
    s,e = map(int,sys.stdin.readline().split())
    
    print(dp[e]-dp[s-1])
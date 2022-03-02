# 플로이드 와샬의 기본 개념은 i에서 출발해 j로 가는 경로의 가중치를 저장하는 2차원 배열을 채우는데,
# i를 출발해 j로 바로 가는 것보다 k를 거쳐 j로 가는 게 효율적일 경우(저렴할 경우) 해당 값을 갱신해준다.
# k의 값을 가장 바깥 for문에서 반복해주므로 하나의 경유지 k만 거치는 것뿐만 아니라 여러 경유지를 거치는 경로또한 포함한다.
# k : 경유지
# for k in range(1, v+1):
#     # i : 출발지
#     for i in range(1, v+1):
#         # j : 목적지
#         for j in range(1, v+1):
#             dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
# <출처 : https://seoyoung2.github.io/algorithm/2020/07/22/Floyd-Warshall.html>



INF = 987654321
n = int(input())
m = int(input())

dist = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    # dist[a][b] = c
    dist[a][b] = min(dist[a][b],c)

for k in range(1,n+1):
    dist[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == INF:
            dist[i][j] = 0
        print(dist[i][j], end=" ")
    print()
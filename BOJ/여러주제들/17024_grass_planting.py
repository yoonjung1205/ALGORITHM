# N = int(input())
# adj = [[0]*(N+1) for _ in range(N+1)]
# for _ in range(N-1):
#     f1,f2 = map(int,input().split())
#     adj[f1][f2] = 1
#     adj[f2][f1] = 1
#
# ans = 0
# for i in range(N+1):
#     cnt = 0
#     for j in range(N+1):
#         if adj[i][j] == 1:
#             cnt += 1
#             if ans < cnt:
#                 ans = cnt
#
# print(ans+1)

N = int(input())
adj = [[] for _ in range(N+1)]
# print(adj)
for _ in range(N-1):
    f1,f2 = map(int,input().split())
    adj[f1].append(f2)
    adj[f2].append(f1)

ans = 0
for i in range(N+1):
    tmp = len(adj[i])
    if ans < tmp:
        ans = tmp

print(ans+1)
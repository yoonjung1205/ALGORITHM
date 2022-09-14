# 시간초과 해결못함

from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())

alpha_info = list(input())
alpha_info.insert(0,0)
info = [[] for _ in range(N+1)]
for i in range(N-1):
    e1, e2 = map(int,input().split())
    info[e1].append(e2)
    info[e2].append(e1)

# print(alpha_info)
# print(info)
visit = [0] * (N+1)
result = ''
# def bfs(s,handle):
#     global result
#     q = deque()
#     q.append([s,handle])
#
#     while q:
#         v, handle = q.popleft()
#
#         for i in info[v]:
#             if not visit[i]:
#                 visit[i] = 1
#                 q.append([i,handle + alpha_info[i]])
#
#             elif len(info[v]) == 1:
#                 if result <= handle:
#                     result = handle


def dfs(s,handle):
    global result
    visit[s] = 1

    for i in info[s]:
        if not visit[i]:
            dfs(i,handle+alpha_info[i])
        elif len(info[s])==1:
            if result <= handle:
                result = handle
            print(result)
dfs(1,alpha_info[1])
# bfs(1,alpha_info[1])
print(result)


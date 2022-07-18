from collections import deque
import sys
input = sys.stdin.readline
T = int(input())


# def bfs(s):
#     global result
#     q = deque()
#     q.append(s)
#     visit[s]=[1,'b']
#
#     while q:
#         now = q.popleft()
#         for t in adj[now]:
#             if not visit[t]:
#                 if (visit[now][0]+1)%2 != 0:
#                     visit[t]=[visit[now][0]+1,'b']
#                 else:
#                     visit[t]=[visit[now][0] + 1, 'w']
#
#                 q.append(t)
#             if visit[now][1] == visit[t][1]:
#                 result = 'NO'
#                 return

def bfs(s):
    global result
    q = deque()
    q.append(s)
    visit[s]='b'

    while q:
        now = q.popleft()
        for t in adj[now]:
            if not visit[t]:
                if visit[now] == 'b':
                    visit[t]='w'
                else:
                    visit[t]='b'

                q.append(t)
            if visit[now] == visit[t]:
                result = 'NO'
                return

for _ in range(T):
    result = 'YES'
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int,input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)
    visit = [0] * (V + 1)
    for i in range(1,V+1):
        if not visit[i]:
            bfs(i)
        if result == 'NO':
            break

    print(result)


'''
1
5 4
1 2
3 4
4 5
3 5
'''
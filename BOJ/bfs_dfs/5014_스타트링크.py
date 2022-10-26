from collections import deque

F,S,G,U,D = map(int,input().split())
result = "use the stairs"
visit = [0] * (F+1)
def bfs(start, count):
    global result, now
    q = deque()
    q.append([start,count])

    while q:
        now, cnt = q.popleft()
        nu = now + U
        nd = now - D
        if now == G:
            result = cnt
            return
        elif not visit[now] and (1 <= nu <= F or 1 <= nd <= F):
            visit[now] = 1
            if 1 <= nu <= F:
                q.append([nu,cnt + 1])
            if 1 <= nd <= F:
                q.append([nd,cnt + 1])

bfs(S,0)


print(result)
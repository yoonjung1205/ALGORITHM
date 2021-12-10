from collections import deque
N,K = map(int,input().split())

def search(N,K):
    q = deque()
    q.append([N,0]) # N값과 연산 몇번했는지 카운트해줄 변수
    visit[N] = 1

    while q:
        t,c = q.popleft()
        if t == K:
            return c
        for x in [t-1,t+1,2*t]:
            if 0 <= x <= 100000 and not visit[x]:
                q.append([x,c+1])
                visit[x] = 1
       
'''

def calc(n):
    q = deque()
    q.append(n)
    while q:
        if visited[M]:
            return
        t = q.popleft()
        for i in [t+1,t-1,t*2]:
            if 0 <= i <= 100001 and visited[i] == 0:
                visited[i] = visited[t] + 1     # visited에 연산횟수 카운팅해서 집어넣기
                q.append(i)

print(visit[M])

'''    

visit= [0] * 100001
print(search(N,K))

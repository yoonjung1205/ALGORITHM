from collections import deque

def bfs(x,y):
    global result
    q = deque()
    q.append([x,y])
    visit.append([x,y])
    while q:
        r,c = q.popleft()
        if r == position[-1][0] and c == position[-1][1]:
            result = 'happy'
            return 
        for sx,sy in position[1:]:   # 편의점
            distance = abs(r-sx) + abs(c-sy)    # 맨하튼 거리
            if distance <= 1000 and [sx,sy] not in visit:
                q.append([sx,sy])
                visit.append([sx,sy])

    result = 'sad'
    return 

t = int(input())
for tc in range(t):
    n = int(input())    # 편의점 개수
    position = [list(map(int,input().split())) for _ in range(n+2)]   # 입력받은 위치 좌표들     
    visit = []
    result =''

    bfs(position[0][0],position[0][1])
    print(result)



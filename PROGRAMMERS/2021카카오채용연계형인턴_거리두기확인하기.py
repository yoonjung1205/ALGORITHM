from collections import deque

# # print(visited)
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# def bfs(place):
#     start = []
#     for i in range(5):
#         for j in range(5) :
#             if place[i][j] == 'P':
#                 start.append([i,j])
#     for sta in start:
#         visited = [[0]*5 for _ in range(5)]
#         distance = [[0]*5 for _ in range(5)]
#         q = deque()
#         q.append(sta)
#         visited[sta[0]][sta[1]] = 1
#         while q:
#             x,y = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
#                     if place[nx][ny] == 'O':
#                         visited[nx][ny] = 1
#                         distance[nx][ny] = distance[x][y] + 1
#                         q.append([nx,ny])
#                     if place[nx][ny] == 'P' and distance[x][y] <= 1:                
#                         return 0
#     return 1

# def solution(places):
#     answer = []
#     # 맨해튼 거리 = |r1-r2|+|c1-c2| <= 2
#     for place in places:    
#         answer.append(bfs(place))
                
#     return answer

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, place):
    queue = deque([[x, y]])
    visited = [[False for _ in range(5)] for _ in range(5)]
    depth = 0
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True
                if place[nx][ny] == 'P':
                    return 0
                elif place[nx][ny] == 'O':
                    if depth < 1:
                        queue.append([nx, ny])
        depth += 1
    return 1
    
def solution(places):
    answer = []
    
    for place in places:
        tmp = 1
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                     tmp = bfs(x, y, place)
                if tmp == 0:
                    break 
            if tmp == 0:
                break  
        answer.append(tmp)
    return answer
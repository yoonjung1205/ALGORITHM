import sys
sys.stdin = open('input.txt')

# # 우하좌상
# dr = [0,1,0,-1]
# dc = [1,0,-1,0]
#
# pipe = [[0,0,0,0],
#         [1,1,1,1], #상하좌우
#         [0,1,0,1], #상하
#         [1,0,1,0], #좌우
#         [1,0,0,1], #상우
#         [1,1,0,0], #하우
#         [0,1,1,0], #하좌
#         [0,0,1,1]] #상좌
#
#
# T = int(input())
#
# for tc in range(1,T+1):
#     N,M,R,C,L = map(int,input().split())
#
#     # 지도 정보
#     tunnel = [list(map(int,input().split())) for _ in range(N)]
#     visited = [[0] * M for _ in range(N)]
#
#     Q = [(R,C)]
#     visited[R][C] = 1
#
#     ans = 0
#
#     while Q:
#         r, c = Q.pop(0)
#         ans += 1
#
#         if visited[r][c] >= L: continue
#
#         # 사방향 탐색
#         for d in range(4):
#             # 현재 바라보는 방향으로 길이 없으면
#             curr_p = tunnel[r][c]
#             if pipe[curr_p][d] == 0: continue
#
#             nr = r + dr[d]
#             nc = c + dc[d]
#             # 다음좌표가 맵을 벗어났다면,
#             if nr < 0 or nr >= N or nc <0 or nc>=M: continue
#
#             # 바라보는 방향
#             nd = (d+2)%4
#             # 다음 파이프 모양
#             np = tunnel[nr][nc]
#
#             # 방문을 했거나, 다음좌표의 파이프가 현재좌표와 연결되지 않으면
#             if visited[nr][nc] or pipe[np][nd] == 0: continue
#
#             visited[nr][nc] = visited[r][c] + 1
#             Q.append((nr,nc))
#
#     print('#{} {}'.format(tc,ans))

######################################################################
# 우하좌상
# dr = [0,1,0,-1]
# dc = [1,0,-1,0]
#
# pipe = [[0,0,0,0],
#         [0,1,2,3], #상하좌우
#         [1,3], #상하
#         [0,2], #좌우
#         [0,3], #상우
#         [0,1], #하우
#         [1,2], #하좌
#         [2,3]] #상좌
#
# T = int(input())
#
# for tc in range(1,T+1):
#     N,M,R,C,L = map(int,input().split())
#
#     # 지도 정보
#     tunnel = [list(map(int,input().split())) for _ in range(N)]
#     visited = [[0] * M for _ in range(N)] # 방문체크
#
#     Q = [(R,C,1)]
#     visited[R][C] = 1
#
#     ans = 0
#
#     while Q:
#         r,c,time = Q.pop(0)
#         ans += 1
#         if time >= L: continue
#
#         curr_p = tunnel[r][c]
#         for i in pipe[curr_p]:
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
#             if tunnel[nr][nc] == 0 or visited[nr][nc]: continue
#
#             if (i+2)%4 in pipe[tunnel[nr][nc]]: # 연결이 되어있는지 확인
#                 Q.append((nr,nc,time+1))
#                 visited[nr][nc] = 1
#
#     print('#{} {}'.format(tc, ans))
#######################################################################
# 우하좌상
dr = [0,1,0,-1]
dc = [1,0,-1,0]

pipe = [[0,0,0,0],
        [0,1,2,3], #상하좌우
        [1,3], #상하
        [0,2], #좌우
        [0,3], #상우
        [0,1], #하우
        [1,2], #하좌
        [2,3]] #상좌


def dfs(r,c,time):
    visited[r][c] = time
    if time == L: return

    for i in pipe[tunnel[r][c]]:
        nr = r+dr[i]
        nc = c+dc[i]

        # tunnel[nr][nc] 땅이 아닌지
        if 0<=nr<N and 0<=nc<M and tunnel[nr][nc] and ((i+2)%4 in pipe[tunnel[nr][nc]]) and visited[nr][nc] > time:
            dfs(nr,nc,time+1)



T = int(input())

for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())

    # 지도 정보
    tunnel = [list(map(int,input().split())) for _ in range(N)]
    visited = [[987654321] * M for _ in range(N)] # 방문체크

    dfs(R,C,1)

    ans = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] != 987654321:
                ans += 1

    print('#{} {}'.format(tc,ans))
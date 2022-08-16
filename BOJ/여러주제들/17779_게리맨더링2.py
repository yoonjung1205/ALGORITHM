from pprint import pprint

N = int(input())
JH = [[0]+list(map(int,input().split())) for _ in range(N)]
JH.insert(0,[0]*(N+1))
g = [[0]*(N+1) for _ in range(N+1)]

minValue = 10000000
for x in range(1,N-1):
    for y in range(2,N):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if 1 < x + d1 + d2 <= N:
                    if 1 <= y - d1 and y + d2 <= N:
                        places = [0] * 5
                        for r in range(1,N+1):
                            for c in range(1,N+1):
                                # 5선거구
                                if r+c >= x+y and r+c <= x+y+2*d2 and r-c >= x-y and r-c <= x-y +2*d1 :
                                    places[4] += JH[r][c]
                                    g[r][c] = 5

                                # 1선거구
                                elif 1 <= r < x+d1 and 1 <= c <= y:
                                    places[0] += JH[r][c]
                                    g[r][c] = 1

                                # 2선거구
                                elif 1 <= r <= x+d2 and y < c <= N:
                                    places[1] += JH[r][c]
                                    g[r][c] = 2

                                # 3선거구
                                elif x+d1 <= r <= N and 1 <= c < y-d1+d2:
                                    places[2] += JH[r][c]
                                    g[r][c] = 3

                                # 4선거구
                                elif x+d2 < r <= N and y-d1+d2 <= c <= N:
                                    places[3] += JH[r][c]
                                    g[r][c] = 4


                        if minValue >= max(places) - min(places):
                            minValue = max(places) - min(places)
                        pprint(g)

print(minValue)

# import sys
# from pprint import pprint
#
# input = sys.stdin.readline
# '''
# 선거구를 나누는 방법은 다음과 같다.
# 기준점 (x, y)와 경계의 길이 d1, d2를 정한다. (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
# 다음 칸은 경계선이다.
# (x, y), (x+1, y-1), ..., (x+d1, y-d1)
# (x, y), (x+1, y+1), ..., (x+d2, y+d2)
# (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
# (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
# 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.
# 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
# 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
# 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
# 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
# 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
# '''
#
# N = int(input())
# arr = [list(map(int, input().split())) for i in range(N)]
#
#
# # x: 기준점 행, y: 기준점 열, d1, d2는 경계의 길이
# # x, y, d1, d2를 인자로 전달하면 인구 최대 - 인구 최소를 리턴
# def divide(x, y, d1, d2):
#     people = [0 for i in range(6)]
#     # temp = [[0 for i in range(N)] for j in range(N)]
#     for i in range(N):
#         for j in range(N):
#             # 1구역: 기준열포함 왼쪽열, 기준행 + d1보다 윗행, 기준점으로 부터 왼쪽밑으로 뻗는 대각선 경계
#             if j <= y and i < x + d1 and i + j < x + y:
#                 people[1] += arr[i][j]
#                 # temp[i][j] = 1
#             # 2구역: 기준열보다 오른쪽열, 기준행 + d2포함 윗행, 기준점으로 부터 오른쪽밑으로 뻗는 대각선 경계
#             elif j > y and i <= x + d2 and (i - j) < (x - y):
#                 people[2] += arr[i][j]
#                 # temp[i][j] = 2
#             # 3구역: 기준열 + d2 - d1 보다 왼쪽열, 기준행 + d1포함 아래행, 오른쪽밑으로 뻗는 대각선 경계
#             elif j < y + d2 - d1 and i >= x + d1 and (i - j) > (x - y + 2 * d1):
#                 people[3] += arr[i][j]
#                 # temp[i][j] = 3
#             # 4구역: 기준열 + d2 - d1 포함 오른쪽열, 기준행 + d2보다 아래행, 왼쪽밑으로 뻗는 대각선 경계
#             elif j >= y + d2 - d1 and i > x + d2 and i + j > x + y + 2 * d2:
#                 people[4] += arr[i][j]
#                 # temp[i][j] = 4
#             # 5구역: 나머지
#             else:
#                 people[5] += arr[i][j]
#     #             temp[i][j] = 5
#     # pprint(temp)
#     return max(people[1:]) - min(people[1:])
#
#
# ans = 99999999999
# for x in range(N):
#     for y in range(N):
#         for d1 in range(1, N):
#             for d2 in range(1, N):
#                 # if x - d1 >= 0 and x + d2 < N and y + d1 + d2 < N:
#                 if x + d1 + d2 < N and y >= d1 and y < N - d2:
#                     ans = min(ans, divide(x, y, d1, d2))
# # divide(1, 3, 2, 2)
# print(ans)
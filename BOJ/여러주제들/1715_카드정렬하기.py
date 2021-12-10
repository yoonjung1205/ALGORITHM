import heapq

N = int(input())
card = []

for _ in range(N):
    heapq.heappush(card, int(input()))
total = 0
while len(card) > 1:
    tmp1 = heapq.heappop(card)
    tmp2 = heapq.heappop(card)
    # print(tmp1, tmp2)
    heapq.heappush(card, tmp1+tmp2)
    total += tmp1+tmp2
    # print(card)

print(total)
# print(card)

# def calc(cur):
#     global ans
#     if cur == N:
#         total = 0
#         arr = []
#         # print(arr2)
#         for i in range(N):
#             total += arr2[i]
#             arr.append(total)
#         # print(arr)
#         result = arr[-1] + arr[-2]
#         if ans >= result:
#             ans = result
#         return
#
#     for i in range(N):
#         if visited[i]:
#             continue
#
#         visited[i] = 1
#         arr2[cur] = card[i]
#         calc(cur+1)
#         visited[i] = 0
#
#
# visited = [0] * N
# arr2 = [0]*N
# ans = 987654321
#
#
# calc(0)
#
# print(ans)

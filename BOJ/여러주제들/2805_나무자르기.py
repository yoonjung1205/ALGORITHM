import sys
input = sys.stdin.readline


N, M = map(int, input().split())
tree = list(map(int, input().split()))

# h = (M+tree[-1])//2
# before_total = 0
#
# while 1:
#     total = 0
#     for i in range(len(tree)):
#         if tree[i] >= h:
#             total += (tree[i]-h)
#             if total >= M:
#                 h += 1
#                 before_total = total
#                 break
#     if before_total and total < M:
#         print(h-1)
#         quit()


start = 0
end = max(tree)

while start <= end:
    total = 0
    mid = (start + end)//2

    for i in range(N):
        if tree[i] >= mid:
            total += tree[i] - mid
            if total >= M:
                break

    if total >= M:
        start = mid + 1

    elif total < M:
        end = mid - 1

print(end)

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    tree = list(map(int,input().split()))
    # print(tree)
    arr = deque()
    tree.sort()

    if N % 2 == 0:
        for i in range(0,N-1,2):
            arr.append(tree[i])
            arr.appendleft(tree[i+1])
    else:
        for i in range(0,N-1,2):
            arr.append(tree[i])
            arr.appendleft(tree[i+1])
        arr.append(tree[-1])
    ans = 0
    for i in range(N-1):
        cal = abs(arr[i]-arr[i+1])
        if ans < cal:
            ans = cal
    print(ans)



###########################################################
# 구글 블로그 https://namhandong.tistory.com/100
# 정렬 후 인덱스 차이가 2 나게 값 계산하는게 best
# T = int(input())
# for i in range(T):
#     N = int(input())
#     trees = list(map(int,input().split()))
#     trees.sort()
#     result = 0
#     for j in range(2,N):
#         result = max(result, abs(trees[j]-trees[j-2]))
#     print(result)

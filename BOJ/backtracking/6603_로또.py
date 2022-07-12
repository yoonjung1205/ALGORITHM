arr = [0] * 6
# def recur(cur):
#     if cur == 6:
#         if arr != sorted(arr):
#             return
#         print(*arr)
#         return
#
#     for i in range(l):
#         if visited[i] == 0:
#             visited[i] = 1
#             arr[cur] = S[i]
#             recur(cur+1)
#             visited[i] = 0

def recur(cur,start):
    if cur == 6:
        print(*arr)
        return

    for i in range(start,l):
        arr[cur] = S[i]
        recur(cur+1,i+1)


while True:
    S = list(map(int,input().split()))
    l = S[0]
    visited = [0] * l
    if l == 0:
        break
    S = S[1:]
    # print(S)

    # recur(0)
    recur(0,0)
    print()





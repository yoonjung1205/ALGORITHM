N = int(input())

arr = list(map(int,input().split()))
##########################################
# 당연히 시간초과
tmp = [-1]*N
ans = 0
for i in range(N-1):
    for j in range(i,N):
        if arr[i] < arr[j]:
            ans = arr[j]
            tmp[i] = ans
            break

print(*tmp)

#########################################
# 스택 활용(모노톤 스택)
idx = []
idx.append(0)
tmp = [-1]*N
for i in range(N):
    while idx and arr[i] > arr[idx[-1]]:
        tmp[idx.pop()] = arr[i]
    idx.append(i)

print(*tmp)

########################################
# 스택 활용2
stack = []
tmp = [-1] * N

for i in range(N):
    if len(stack) == 0 or stack[-1] > arr[i]:
        stack.append(arr[i])

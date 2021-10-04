N = int(input())
level = []
for i in range(N):
    level.append(int(input()))

temp = level[-1]
cnt = 0
for i in range(N-2,-1,-1):
    while level[i] >= temp:
        level[i] -= 1
        cnt += 1
    temp = level[i]

print(cnt)
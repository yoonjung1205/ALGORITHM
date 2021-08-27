N = int(input())
p = [int(input()) for _ in range(N)]

cnt = 0
i = 1
while p[0] != max(p):
    if p[i] == max(p[1:]):
        p[i] -= 1
        p[0] += 1
        cnt += 1
    i += 1
    if i == len(p):
        i = 1

for i in range(1,len(p)):
    if p[0] == p[i]:
        cnt += 1
        break
print(p,cnt)
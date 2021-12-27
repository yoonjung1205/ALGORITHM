N,K,B = map(int, input().split())
light = [-1] + list(range(1,N+1))
for i in range(B):
    light[int(input())] = 0

# print(light[1:])

ans = 9999
for start in range(1,N-K+2):
    cnt = 0
    end = start

    for i in range(K):
        if light[end] == 0:
            cnt += 1
        end += 1
    if ans > cnt:
        ans = cnt

print(ans)
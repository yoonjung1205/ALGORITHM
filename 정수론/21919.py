N = int(input())
A = list(map(int,input().split()))
ans = 1
flag = 0
for i in range(2,A[N-1]):
    if i * i > A[N-1]:
        break
    for j in range(N):
        if A[j] % i == 0:
            print(A[j])
            ans *= A[j]
            break
if ans == 1:
    print(-1)
else:
    print(ans)

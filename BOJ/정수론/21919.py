N = int(input())
A = set(map(int,input().split()))
A = list(A)

ans = 1
for i in range(len(A)):
    flag = 0
    for j in range(2,A[i]+1):
        if j * j > A[i]:
            break
        if A[i] % j == 0:
            flag = 1
            break
        
    if flag == 0:
        ans *= A[i]

if ans == 1:
    print(-1)
else:
    print(ans)

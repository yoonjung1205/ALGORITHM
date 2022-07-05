# permutation, 재귀 쓰면 -> 메모리초과, 시간초과 남

N = int(input())
temp = list(map(int,input().split()))

for i in range(N-1,0,-1):
    if temp[i] > temp[i-1]:
        for j in range(N-1,0,-1):
            if temp[j] > temp[i-1]:
                temp[j],temp[i-1] = temp[i-1],temp[j]
                temp = temp[:i] + sorted(temp[i:])
                print(*temp)
                exit()

print(-1)
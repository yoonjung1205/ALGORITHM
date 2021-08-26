N, M = map(int,input().split())
result = []
rresult = []
for i in range(N):
    result.append(list(input()))
    
for i in range(N):    
    for j in range(M):
        for k in range(min(N,M)):
            if ((i + k) < N) and ((j + k) < M) and (result[i][j] == result[i][j+k] == result[i+k][j] == result[i+k][j+k]):
                rresult.append((k+1)**2)
        

print(max(rresult))

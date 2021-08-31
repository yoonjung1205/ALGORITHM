N = int(input())
w = list(map(int,input().split()))
w.sort()
total = 1

for i in range(N):
    if total < w[i]:
        break
    total += w[i]
    
print(total+1)
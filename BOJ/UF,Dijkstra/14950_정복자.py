def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[y] > rank[x]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1

N,M,t = map(int,input().split())

arr = []
parent = list(range(N+1))
rank = [0] * (N+1)

for i in range(M):
    A,B,C = map(int,input().split())
    arr.append([A,B,C])

arr.sort(key=lambda x: x[2])

# print(arr)
ans = 0
cnt = 0
for i in range(len(arr)):
    c1 = arr[i][0]
    c2 = arr[i][1]
    w = arr[i][2]

    if find(c1) == find(c2):
        continue

    ans += (w + t*cnt)
    union(c1, c2)
    cnt += 1

    # 한 번 정복한 도시는 다시 정복하지 않는다.
    if cnt == N-1:
        break

print(ans)
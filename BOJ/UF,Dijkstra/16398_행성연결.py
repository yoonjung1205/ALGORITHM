def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)

    if rank[x] > rank[y]:
        parent[y] = x # y는 x를 부모노드로
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

# print(arr)
temp = []
for i in range(N):
    for j in range(i,N):
        if arr[i][j]:
            temp.append([i,j,arr[i][j]])

temp.sort(key= lambda x:x[2])

parent = list(range(N))
rank = [0] * N
ans = 0
for i in range(len(temp)):
    x = temp[i][0]
    y = temp[i][1]
    w = temp[i][2]

    if find(x) == find(y):
        continue
    ans += w
    union(x,y)        

print(ans)
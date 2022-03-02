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
M = int(input())

arr = [0] * N
for i in range(N):
    tmp = list(map(int,input().split()))
    arr[i] = tmp

# print(arr)

parent = list(range(N))
rank = [0] * N

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:  # 도시들이 인접했으면, union함
            union(i,j)

tour = list(map(int,input().split()))

result = []
for city in tour:
    result.append(find(city-1)) # 각 도시의 부모노드를 찾아서 result에 append(인덱스 번호랑 맞춰주기 위해서 -1해줌)

# print(result)
if len(set(result)) == 1:
    print('YES')
else:
    print('NO')
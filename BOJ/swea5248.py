def find(x): #x의 루트를 반환하는 연산
    if parent[x] == x : # x의 부모가 누구냐? -> x => 루트를 반환!
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x,y): # x가 속한 집합, y가 속한 집합을 합치는 연산
    x = find(x)
    y = find(y)
    parent[x] = y
    if rank[x] > rank[y]:   # rank가 낮은 집합(y)을 낮은 집합에 붙인다. 
        parent[y] = x
    elif rank[y] > rank[x]:
        parent[x] = y
    else:   # rank가 같을때는 부모가 된 y의 rank를 1 늘려준다.
        parent[x] = y
        rank[y] += 1


N,M = map(int,input().split())
temp = list(map(int, input().split()))

parent = list(range(N+1))
rank = [1 for i in range(N+1)]

for i in range(0, 2*M, 2):
    if find(temp[i]) == find(temp[i+1]): # 이미 연결되어 있다면? pass!
        continue
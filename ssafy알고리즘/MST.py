# PRIM
INF = 987654321
def PRIM(start,V):
    key = [INF] * V # MST에 연결된 노드들의 가중치들
    MST = [0] * V
    
    key[start]=0

    for _ in range(V): # V번 반복
        u = 0
        minV = INF
        for i in range(V): # 
            if MST[i] == 0: # MST에 포함되지 않으면서,
                if key[i] < minV: # 가중치가 가장 작은 노드를 u에 대입
                    minV = key[i]
                    u = i
        MST[u] = 1 # MST에 u 포함
        for v in range(V):
            if MST[v] == 0 and adj[u][v] != 0: # MST에 포함되지 않으면서, u에 인접한 v에 대해
                if key[v] > adj[u][v]: # 저장되어있던 가중치 값이, 더 크면 갱신해준다.
                    key[v] = adj[u][v]

def prim(start,V):
    key = [INF] * (V+1)
    MST = [0] * (V+1)
    key[start] = 0

    for _ in range(V):
        u = 0
        minV = INF
        for i in range(V+1):
            if MST[i] == 0 and minV > key[i]:
                minV = key[i]
                u = i
        MST[u] = 1
        for v in range(V+1):
            if MST[v] == 0 and adj[u][v] != 0:
                if key[v] > adj[u][v]:
                    key[v] = adj[u][v]

# KRUSKAL
def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x,y):
    x=find(x)
    y=find(y)

    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1

V = 6
parent = [i for i in range(V+1)]
rank = [0] * (V+1)

tmp = [] # [[n1,n2,w],...]
tmp.sort(key=lambda x:x[2]) # 가중치를 기준으로 오름차순 정렬
answer = 0 # 가중치 합 담을 변수
for arr in tmp:
    if find(arr[0]) != find(arr[1]): # 싸이클이 생기지 않으면,
        union(arr[0],arr[1])
        answer += arr[2]

def find(x):
    if parent[x] == x:
        return x
    else:
        find(parent[x])

def union(x,y):
    x = find(x)
    y = find(y)

    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1

for arr in tmp:
    if find(arr[0]) != find(arr[1]):
        union(arr[0],arr[1])
        answer += arr[2]

# Dijkstra
def DIJKSTRA(start,V):
    U = [0] * (V+1)
    U[start] = 1
    for i in range(V+1):
        D[i] = adj[start][i]

    for _ in range(V):
        u = 0
        minV = INF
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                u = i
        U[u] = 1
        for v in range(V+1):
            if 0 < adj[u][v] < INF:
                D[v] = min(D[v], D[u]+adj[u][v])

adj = [[INF]*(V+1) for _ in range(V+1)] # 초기화를 이렇게 해놓고 인접행렬 만들기
for i in range(V+1):
    adj[i][i] = 0
D = [0] * (V+1)
print(D) # 시작지점에서 각 정점으로 가는 최소비용


def dijkstra(start,V):
    U = [0] * (V+1)
    U[start] = 1
    for i in range(V+1):
        D[i] = adj[start][i]
    for _ in range(V):
        u = 0
        minV = INF
    
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                u = i
        U[u] = 1
        for v in range(V+1):
            if 0 < adj[u][v] < INF:
                D[v] = min(D[v], D[u]+adj[u][v])



# m, n = map(int, input().split())
# arr = []

# def recur(cur, cnt):
#     if cnt == n:
#         for i in range(n):
#             print(arr[i], end = ' ')
#         print("")
#         return

#     if cur == m + 1:
#         return

#     arr.append(cur)
#     recur(cur + 1, cnt + 1)
#     arr.pop()
#     recur(cur + 1, cnt)

# recur(1, 0)


# 병합정렬
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]
    return merge(left,right)

def merge(left,right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# 퀵정렬
# Hoare
def partition(arr,l,r):
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i<=j and arr[i]<=p:
            i+=1

        while i<=j and arr[j]>=p:
            j-=1
        if i<j: arr[i],arr[j] = arr[j],arr[i]
    arr[l],arr[j] = arr[j],arr[l]
    return j

def quick_sort(arr,l,r):
    if l<r:
        s=partition(arr,l,r)
        quick_sort(arr,l,s-1)
        quick_sort(arr,s+1,r)

# Lomuto
def partition(arr,l,r):
    p = arr[r]
    i = l-1
    for j in range(l,r):
        if arr[j] <= p:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i+1


# 병합정렬
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        while left[i] < right[j]:
            result.append(left[i])
            i += 1

        while left[i] > right[j]:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# 퀵 정렬
# Hoare
def partition(arr,l,r):
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i<=j and arr[i] <= p:
            i += 1

        while i<=j and arr[j] >= p:
            j -= 1
        if i<j: arr[i],arr[j] = arr[j],arr[i]

    arr[l],arr[j] = arr[j],arr[l]
    return j

# Lomuto
def partition(arr,l,r):
    p = arr[r]
    i = l-1
    for j in range(l,r):
        if arr[j] <= p:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i+1

def quick_sort(arr,l,r):
    if l<r:
        s = partition(arr,l,r)
        quick_sort(arr,l,s-1)
        quick_sort(arr,s+1,r)
# 그래프&백트래킹

완전그래프 : 정점들에 대해 가능한 모든 간선들을 가진 그래프

간선수 (n*(n-1))/2



무방향그래프

노드수 = 간선의 수 * 2

각 정점의 노드 수 = 정점의 차수



방향그래프

노드수 = 간선의 수

각 정점의 노드 수 = 정점의 진출 차수



```python
# 인접
'''
마지막 정점번호, 간선 수
6 8
0 1 0 2 0 5 0 6 4 3 5 3 5 4 6 4
'''
V,E = map(int,input().split())
edge = list(map(int,input().split()))

# 인접그래프
adjM = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1 # 무향 그래프인 경우

# 인접리스트
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1,n2 = edge[2*i], edge[2*i+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)	# 무향 그래프인 경우
```



그래프 순회(탐색)

DFS & BFS

```python
s = [] # stack
visited = []
def dfs(v):
	push(s,v)
    while s:
        v = pop(s)
        if not visted[v]:
            visited[v] = 1
            for each w in adjacency(v):
                if not visited[w]:
                    push(s,w)
                   
def dfs(v):
	push(s,v)
    visited[v] = 1
    while s:
        v = pop(s)
        print(v)
        for each w in adjacency(v):
            if not visited[w]:
                push(s,w)
                vistied[v] = 1
```





# 서로소 집합(Disjoint-sets)

### 상호 배타 집합 표현 - 트리

하나의 집합을 하나의 트리로 표현

자식 노드가 부모 노드를 가리키면 루트 노드가 대표자가 된다.



Make_Set(x) : 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

```python
def Make_Set(x):
    p[x] = x
```

Find_Set(x) : x를 포함하는 집합을 찾는 연산

```python
def Find_Set(x):
    if x == p[x]: return x
    else: return Find_Set(p[x])
    # else: return p[x] = Find_Set(p[x])
    
def Find_Set(x):    
    if x != p[x]:
        p[x] = Find_set(x)
    return p[x]

def Find_Set(x):
    while x != p[x]:
    	x = p[x]
    return x
```

Union(x,y) : x와 y를 포함하는 두 집합을 통합하는 연산

```python
def Union(x,y):
    p[Find_Set(y)] = Find_set(x)
    
    
def Union(x,y):
    x = Find_Set(x)
    y = Find_Set(y)
    
    if rank[x] >= rank[y]: # rank는 트리의 높이
        p[y] = x
    else:
        p[x] = y
    if rank[x] == rank[y]:
    	rank[x] += 1
```



## 최소 신장 트리(MST)

그래프에서 최소 비용 문제

- 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
- 두 정점 사이의 최소 비용의 경로 찾기



신장트리

- n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리



최소 신장 트리(Minimum Spanning Tree)

- 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리



### Prim 알고리즘

하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식

1) 임의 정점을 하나선택해서 시작
2) 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
3) 모든 정점이 선택될 때 까지 1,2 과정 반복



서로소인 2개의 집합 정보를 유지

- 트리 정점들 - MST를 만들기 위해 선택된 정점들
- 비트리 정점들 - 선택되지 않은 정점들



```python
def MST_PRIM(start,V):
    key = [INF] * (V+1)
    key[start] = 0
    MST = [0] * (V+1)
    pi = [0] * (V+1)
    for _ in range(V):
        u = 0
        minV = INF
        for i in range(V+1):
            if MST[i] == 0:	# MST에 속하지 않은 것들 중에 최소인 것
                if key[i] < minV:
                    u = i
                    minV = key[i]
        MST[u] = 1
        for v in range(V+1):
            if MST[v] == 0 and adj[u][v] != 0:	# u와 인접인 v의 키값 갱신
            	if key[v] > adj[u][v]:
                    key[v] = adj[u][v]	# u를 이용해 기존에 키값 갱신
                    pi[v] = u
    
```



### KRUSKAL 알고리즘

간선을 하나씩 선택해서 MST를 찾는 알고리즘

1) 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
2) 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가
   - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택 (대표숫자가 다르면 싸이클 안생김)
3)  n-1 개의 간선이 선택될 때 까지 2 반복(n: 그래프 정점의 수)

```python
def MST_KRUSKAL():
    
```



## 최단 경로

### 다익스트라(dijkstra) 알고리즘

음의 가중치를 허용하지 않음

시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식

```python
def Dijkstra(start,A,d):
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
                D[v] = min(D[v], D[u] + adj[u][v])
                
print(D) # 시작점에서 각 지점까지 최단경로 출력
```


# DFS(깊이우선탐색)

비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함 -> DFS,BFS 이용

- 깊이 우선 탐색(Depth First Search)
- 너비 우선 탐색(Breadth First Search)

지나온 지역을 stack에 넣는다

```python
def dfs(s,V):
    visited = [0] * (V+1)
    stack = []
    i = s # 현재 방문한 정점 i 
    visited[i] =1
    print(node[i])
  
    while i != 0: #True
        for w in range(1,V+1):
            if adj[i][w]==1 and visited[w]==0:
                stack.append(i) # 방문 경로 저장
                i=w				# 새 방문지 이동
                visited[w] = 1
                print(node[i])
                break
            else:
                if stack:
                    i = stack.pop()
                else:
                    i = 0
#         A B C D E F G
adj = [[0,0,0,0,0,0,0,0], 
       [0,0,0,0,0,0,0,0], # A
       [0,0,0,0,0,0,0,0], # B
       [0,0,0,0,0,0,0,0], # C
       [0,0,0,0,0,0,0,0], # D
       [0,0,0,0,0,0,0,0], # E
       [0,0,0,0,0,0,0,0], # F
       [0,0,0,0,0,0,0,0]  # G
      ]
```



재귀로 DFS(방향없을때)

```python
# 1. 노드의 갯수(N), 간선의 갯수(M)
n = 7
m = 8

# 2. 인접 행렬(adj[mxN][mxN]), 방문 배열(bool vis[mxN])
adj = [[0 for i in range(n+1)] for j in range(n+1)]
vis = [False for i in range(n+1)]

# 4. 일단 들어오면 방문처리
def dfs(u):
    vis[u] = True

    print(u, end=" ")
    # 4.1 i가 u와 인접행렬이면서 방문하지 않은 곳 dfs 탐색
    for i in range(1, n+1):
        if adj[u][i] and not vis[i]:
            dfs(i)

# 3. 인접 행렬 입력 받기
for i in range(m):
    fr, to = map(int, input().split())
    adj[fr][to] = adj[to][fr] = 1

# 5. 1번 노드에서 dfs시작
dfs(1)
```

순철님 코드

```python
def dfs(s, e):
    visit[s] = 1
    for i in edge[s]:
        if i == e:
            global path
            path = 1
            return
        if not visit[i]:
            dfs(i, e)


for tc in range(1, TC + 1):
    path = 0
    V, E = map(int, input().split())
    edge = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    for i in range(E):
        s, e = map(int, input().split())
        edge[s].append(e)
        # edge[e].append(s) 방향성이 없을때 추가
    s, e = map(int, input().split())
    dfs(s, e)
    print('#{} {}'.format(tc, path))
```


# BFS(Breadth First Search)

너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 형식

거리문제를 풀때 유용하게 사용할 수 있다!

```python
def BFS(G, v):	# 그래프G, 탐색 시작점 v
    visited = [0]*n+1	# 인데스 맞추기 위해 n+1
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:	# 방문되지 않은 곳이라면
            visited[t] = True
            visit(t)	# 정점 t에서 할 일
        	for i in G[t]:	# t와 연결된 모든 정점에 대해
            	if not visited[i]:	# 방문되지 않은 곳이면
                	queue.append(i)
```

``` python
# 노드간 거리를 visited에 이용
def BFS(G, v, n):	# 그래프G, 탐색 시작점 v
    visited = [0]*n+1	# 인데스 맞추기 위해 n+1
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        visit(t)	# 정점 t에서 할 일
        for i in G[t]:	# t와 연결된 모든 정점에 대해
            if not visited[i]:	# 방문되지 않은 곳이면
                queue.append(i)
                visited[i] = visited[t] + 1 # n으로 부터 1만큼 이동
```



<연습문제3>

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, V):
    q = [] 				# 큐 생성
    visited = [0] * V+1	# visited 생성
    q.append(s)			# 시작점 인큐
    visited[s] = 1		# 시작점 visited 표시
    while q:		# 큐가 비어있지 않으면(처리할 정점이 남아있으면)
    	t = q.pop(0)	# 디큐해서 t에 저장
    	print(t)	# t에 대한 처리
    	for i in range(1, V+1):		# t에 인접이고 미방문인 모든 i에 대해
			if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1 
                
def bfs2(s, V):
    q = [] 				# 큐 생성
    visited = [0] * V+1	# visited 생성
    q.append(s)			# 시작점 인큐
    visited[s] = 1		# 시작점 visited 표시
    while q:		# 큐가 비어있지 않으면(처리할 정점이 남아있으면)
    	t = q.pop(0)	# 디큐해서 t에 저장
    	print(t)	# t에 대한 처리
    	for i in adjList[t]:		# t에 인접이고 미방문인 모든 i에 대해
			if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

V, E = map(int,input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]	# 인접행렬
adjList = [[] for _ in range(V+1)]		# 인접리스트

for i in range(E):
    n1, n2 = edge[2*i],edge[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 없으면 방향없는 그래프
	
    adjList[n1].append(n2)
    adjList[n2].append(n1)
bfs(1,V)
bfs2()
```

<아날로그st>

```python
def bfs(s,V):
    q = [0]*V
    front = -1
    rear = -1
    visited = [0]*(V+1)
    rear += 1	# 시작점 인큐
    q[rear] = s
    visited[s] = 1	# 시작점 visited
    while front != rear:
        front += 1
        t = q[front]	# 디큐해서 t에 저장
        print(t)
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited=[i] == 0:
                rear += 1	# 인큐 i
                q[rear] = i
                visited[i] = visited[t] + 1	# i 방문 표시
```




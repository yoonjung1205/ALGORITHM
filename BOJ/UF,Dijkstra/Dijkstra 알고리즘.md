# Dijkstra 알고리즘

> 다익스트라(Dijkstra) 최단거리 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로(최소 가중치)를 구해주는 알고리즘
>
> 음의 가중치가 없을 때만 적용가능 하다



## 알고리즘의 원리

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화 한다.
3. **방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.**
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 3번-4번을 반복한다.



위의 과정에서 각 노드에 대한 현재까지의 최단거리 정보를 항상 1차원 리스트에 저장하면 리스트를 계속 갱신한다. 즉, 지금 처리하고 있는 노드의 주변 간선들을 확인하고 이전까지 보다 더 거리가 짧은 경로를 찾으면 갱신한다.

✔최단거리가 가장 짧은 노드를 선택한다 -> (그리디 알고리즘)



```python
# 다익스트라 알고리즘
INF = 987654321
def Dijkstra(start):
    # 탐색을 했는지 여부 표시할 배열 U
    U = [0] * (V+1)
    U[start] = 1
    for i in range(V+1):
        # 시작점과 인접한 노드들과의 거리를 D 배열에 넣음
        D[i] = adj[start][i]
    for _ in range(V):
        u = 0
        minV = INF
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:	# i에서 최단거리라면
                minV = D[i]	# minV 갱신
                u = i		# 그때의 i를 다음 방문할 노드로 정함
        U[u] = 1
        for v in range(V+1):
            # v가 정점 u와 인접하면,
            if 0 < adj[u][v] < INF:
                # 시작정점에서 u를 거쳐서 v로 가는 것과 v로 가는것의 거리를 비교
                # 짧은 거리를 저장
                D[v] = min(D[v], D[u] + adj[u][v])
                
print(D) # 시작점에서 각 지점까지 최단경로 출력
```



알고리즘의 원리에서 보면 거리가 짧은 노드를 선택하여 방문하는데 이를 이용해 heapq를 사용한 알고리즘도 구상할 수 있다. 파이썬 라이브러리에서는 heapq는 최소힙이므로 사용하기에 적합하다. 

기존 알고리즘과 비슷하지만 연결된 노드를 (거리,노드) 로 묶어 우선순위 큐에 넣어준다는 점이 다르다.

- 최소힙(Min Heap) -> 값이 가장 낮은 데이터가 먼저 삭제된다.
- 힙은 시간복잡도 O(NlogN) , 리스트는 시간복잡도 O(N^2) -> N이 클수록 힙이 유리하다.

```python
# 힙을 이용한 다익스트라 알고리즘
import heapq

INF = 987654321
def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in adj[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


V,E = map(int,input().split())
adj = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
for _ in range(E):
    n1,n2,w = map(int,input().split())
    adj[n1].append([n2,w])  # n1노드에서 n2노드로 가는 거리가 w
    # print(adj)

result = INF
dijkstra(0)

```



+ 백준 1753(최단경로) 풀어볼 예정!
### UF(교재의 Disjoint-sets부분)

#### UF가 뭐야? 딱 세개만 기억해

##### 1. Make-set: 먼저 모든 노드들의 루트가 자기 자신을 가리키도록 설정

```py
par = list(range(n + 1))
```

#### 2. Find(x): x의 루트가 뭐야? 를 리턴해주는 함수

```python
def find(x): 
    if par[x] == x:
        return x
    else:	
        return find(par[x])    
```

###### 시간복잡도를 amortized O(logn)으로 줄여주는 path compression 적용시 (안해도 상관 x)

```python
#path compression
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
```

#### 3. union(x, y): x노드와 y노드가 속한 집합을 연결(합집합)시켜주는 함수

```python
def union(x, y):
    # 1. 먼저 x, y의 루트가 뭔지부터 
    x = find(x)
    y = find(y)
    
	par[x] = y
	# par[y] = x 해도 상관x
```

시간복잡도를 O(logn)으로 줄여주는 union by rank 적용시(안해도 상관 x)

```python
def union_(x, y):
    x = find(x)
    y = find(y)		
    
	# 랭크가 더 적은쪽을 큰쪽 밑에 붙이는거야
    # 그래서 x의 랭크가 더 적을시 x의 부모가 y가 되는 것.
    if rank[x] < rank[y]:
        par[x] = y
    elif rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y
        rank[y] += 1
```



##### UF로 뭘 할수 있냐?

1. 연결요소의 개수 구하기
2. MST(최소신장트리)구하기
   - MST가 뭐야?: **모든 노드들을 연결**할건데 연결된 간선들의 **가중치 합이 최소**가 되도록 연결
   - 크루스칼 알고리즘: 가중치를 오름차순 정렬시켜서 그냥 순서대로 무지성 연결시키면 MST가 된다!
     - 그런데, 연결하려고 하는데 이미 같은 집합내에 있다면? 굳이 연결시킬필요가 없으니 넘어가



1. ###### 연결요소의 개수

```python
# SWEA 5248 그룹나누기
def find(x): # x의 루트를 찾는 함수
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])   # path compression
        return par[x]

def union_(x, y):
    x = find(x)
    y = find(y)

    # union by rank
    if rank[x] > rank[y]:
        par[y] = x
    elif rank[x] < rank[y]:
        par[x] = y
    else:
        par[x] = y
        rank[y] += 1


T = int(input())

for k in range(1, T + 1):
    N, M = map(int, input().split())

    temp = list(map(int, input().split()))
    par = list(range(N + 1))
    rank = [0 for i in range(N + 1)]

    for i in range(0, len(temp), 2):    # 입력으로 받은 쌍들을 전부 union
        union_(temp[i], temp[i + 1])

    arr = []
    for i in range(1, N + 1):   # 각 출석번호를 돌면서 find하면 arr에 각 요소의 루트가 쌓인다
        arr.append(find(i))

    arr = list(set(arr))    # 중복제거 후 프린트해 -> 같은 조에 속했다면 중복된 루트가 append 됐을테니
    print('#{} {}'.format(k, len(arr)))
```



2. ###### MST

```python
# SWEA 5249_최소신장트리

def find(x): # x의 루트를 찾는 함수
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]   # path compression

def union_(x, y):
    x = find(x)
    y = find(y)

    # union by rank
    if rank[x] > rank[y]:
        par[y] = x
    elif rank[x] < rank[y]:
        par[x] = y
    else:
        par[x] = y
        rank[y] += 1

T = int(input())

for k in range(1, T + 1):
    V, E = map(int, input().split())
    par = list(range(V + 1))
    rank = [0 for i in range(V + 1)]

    arr = []
    for i in range(E):
        n1, n2, w = map(int, input().split())
        arr.append([n1, n2, w])

    arr.sort(key= lambda x: x[2])   # 가중치 순으로 오른차순 정렬
    # (크루스칼알고리즘: 각 노드에서 다른 노드로 향하는 가중치중 최소값만을 찾아서 연결하면 MST가 된다는 것을 이용)

    ans = 0
    for i in range(len(arr)):
        n1 = arr[i][0]
        n2 = arr[i][1]
        w = arr[i][2]
        if find(n1) == find(n2): # 이미 연결되 있으면 넘어가
            continue
        ans += w    # 아니라면 가중치 +, 연결시켜
        union_(n1, n2)

    print('#{} {}'.format(k, ans))
```

```python
# SWEA 1251 하나로
def find(x):
    if par[x] == x:
        return x
    else:
        #path compression
        par[x] = find(par[x])
        return par[x]

def union_(x, y):
    x = find(x)
    y = find(y)

    # union by rank
    if rank[x] < rank[y]:
        par[x] = y
    elif rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y
        rank[y] += 1   # rank가 같을때, 루트로 삼은 부분의 rank 증가

T = int(input())

for k in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    par = list(range(N + 1))  # 해당 요소의 부모 요소값
    rank = [0 for i in range(N + 1)]  # 해당 인덱스값이 루트인 트리의 최대 depth

    arr = []
    for i in range(N):
        for j in range(N):
            dis = ((X[i] - X[j]) ** 2) + ((Y[i] - Y[j]) ** 2)
            arr.append((dis, i, j)) # 거리, 섬1, 섬2 정보 싹다 구해서 정렬
    arr.sort(key=lambda x: x[0])	# 크루스칼이니까 거리를 오른차순 정렬해야겠지?

    ans = 0
    for i in range(len(arr)):
        if find(arr[i][1]) == find(arr[i][2]):	# 이미 연결되어있으면 넘어가
            continue
        ans += arr[i][0] * E	# 아니라면 가중치 누적, 연결시켜
        union_(arr[i][1], arr[i][2])

    print('#{} {}'.format(k, round(ans)))

```



#### 다익스트라 (가중치 그래프에서 특정노드에서 특정노드로 가는 최단거리 구하기)

가중치 없으면 BFS 있으면 다익스트라

이거는 어려우니 코드구조를 외우는게 나아

```python
# SWEA 5251 최소이동거리
import heapq 	
# 다익에선 heapq를 사용 사용하는 연산은 딱 두개 -> heapq.heappop(que), heapq.heappush(que,넣고싶은데이터)
# heapq는 최소힙의 자료구조를 가진다, 무슨말이냐? heappop시 que에 있는 데이터중 가장 작은값이 뽑힌다는뜻
# 코드구조는 BFS와 유사

T = int(input())

for k in range(1, T + 1):
    N, E = map(int, input().split())
    temp = [list(map(int, input().split())) for i in range(E)]    # [[s, e, w], ...]
    dist = [9999 for i in range(N + 1)] # 1. 초기 모든 노드 가중치 무한대로 세팅
    v = [[] for i in range(N + 1)]
    for i in temp:
        v[i[0]].append([i[1], i[2]])  # 연결리스트는 단방향, 가중치를 함께저장

    # 2.시작노드 가중치 0으로 세팅하고 출발
    que = []
    heapq.heappush(que, [0, 0])  # 가중치, idx
    dist[0] = 0

    while que:
        d, cur = heapq.heappop(que)  # 가중치중 가장 작은애를 뽑아, 시작~ 현재위치까지 쌓아온 가중치, cur이 현재위치

        if cur == N:
            print('#{} {}'.format(k, d))
            break

        if d > dist[cur]:   # visited 대체
            continue

        # 3. 현재 위치에서 갈 수 있는 위치들을 한번 보자
        # 만약에, 현재까지 쌓아온 가중치 + 현재에서 다음으로가는 가중치가 시작~다음위치까지 가는 가중치보다 작다면 업데이트
        for i in v[cur]:
            nd = d + i[1]	# 시작~다음위치가중치 = 시작~현재위치가중치 + 현재위치~다음위치가중치
            if dist[i[0]] > nd:		# 4. 만약 dist에 저장되어있는 시작~다음위치의 가중치보다 작다면 업데이트
                dist[i[0]] = nd
                heapq.heappush(que, [nd, i[0]]) # 5. 후에 이 노드에서 연결된 다른곳이 있는지 확인하기 위해 최소힙에 넣는다.

```

생길수있는 의문점들

``` tex
왜 heapq써?
다익스트라의 알고리즘 특성상 방문하지 않은 노드중 최소 가중치를 가진 노드를 찾아야하는 로직이 존재한다.
이를 시간복잡도 logn으로 찾기위해 최소힙 자료구조를 사용하는데 이것이 파이썬에서는 heapq가 자동으로 해준다.
heappop하면 알아서 최소값이 pop된다는뜻
```

```tex
if d > dist[cur]:
	continue
이게 왜있어? -> heappop을 하면 최소값이 뽑힌다고 했다. heappop시 해당 노드가 이전에 이미 push됬던 값일 가능성이 있음
무슨말이냐? 만약 4번노드로 가는 다양한 경로들이 존재한다고 생각해보자.

(시작노드 ~ n번노드로 가는 가중치, n노드번호)의 튜플형태로 heappush를 한다
que에 (12,4)(8,4)(6,4) -> (시작노드 ~ 4번노드로 가는 최단거리가 12, 8, 6)가 들어가 있다면?
만약 que에있는 가중치중 (6, 4)가 최소가중치로 pop되었다고 치자.  4번노드로 가는 거리가 6이다 라고 dist배열에 저장을 하겠지? 그러면 나중에 8, 12란 값이 혹시 다시 최소값이 되어서 pop되는 일이 발생되었을때 dist에 저장된 6이란 값보다 큰값(최소비용이 아님)이므로 무시하고 continue할 것(따라서 visited의 역할을 함)
```

```tex
if cur == N:
	print('#{} {}'.format(k, d))
	break
이건 뭐야?
-> 다익스트라 알고리즘의 특성상 내가 heappop해서 최소값을 뽑았다면 그 노드로 가는 다른 최소경로가 존재하지 않는다는게 자명하다고 증명이되어있음. 따라서 도착노드 만나면 바로 답 출력 
```



#### 이번엔 2차원 배열에서의 다익스트라를 보자

```python
# SWEA 5250 최소비용
import heapq
# 가중치가 존재할때 최단경로를 찾는 알고리즘 - 다익스트라
# 알고리즘에서는 heapq(최소힙)를 import해서 사용하여 간단하게 구현 가능
# 코드구조는 BFS와 유사

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())

for k in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    # 1. 모든 지점에서의 가중치를 무한대로 세팅
    dist = [[9999 for i in range(N)] for j in range(N)]

    # 2. 시작지점의 가중치를 0으로 세팅하고 출발
    que = []
    heapq.heappush(que, [0, 0, 0])  # dist, i, j
    dist[0][0] = 0

    while que:
        d, i, j = heapq.heappop(que)

        if i == N - 1 and j == N - 1:
            print('#{} {}'.format(k, d))
            break

        if d > dist[i][j]:  # visited 대체, heappop이 que에서 최소 가중치를 가지는 데이터를 꺼내오므로 그 이전에 들어갔던 데이터가 존재한다면 무시
            continue

        # 3. 현재 위치에서 갈 수 있는 위치들을 한번 보자
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < N and 0 <= nj < N:
                extra = 0 # 추가연료소모량
                if arr[ni][nj] > arr[i][j]: # 더 높은 지역일 경우
                    extra = arr[ni][nj] - arr[i][j]
                nd = d + extra + 1

                # 4. 만약에, 현재까지 쌓아온 가중치 + 현재에서 다음으로가는 가중치가 시작~다음위치까지 가는 가중치보다 작다면 업데이트
                # 처음에 저장되어 있는 시작~ 다음위치의 값들은 전부 무한대로 세팅했으므로 최초로 그 지점을 볼 때는 업데이트 된다.
                # 하지만 나중에 다른 노드를 거쳐서 다시 같은 지점을 가는 경우를 본다면, 지금 이상황이 이전에 왔던 것과 지금 가는것, 그 둘을 비교하는 상황이다
                if dist[ni][nj] > nd:
                    dist[ni][nj] = nd
                    heapq.heappush(que, [nd, ni, nj]) # 5. 후에 이 노드에서 연결된 다른곳이 있는지 확인하기 위해 최소힙에 넣는다.

```


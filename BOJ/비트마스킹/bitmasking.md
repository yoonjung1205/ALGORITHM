# 비트마스킹

### why bitmask?

- **빠른 속도**
- **적은 메모리**



### 비트연산

| 비트 연산자 |        기능        |  문법  |               설명                |
| :---------: | :----------------: | :----: | :-------------------------------: |
|      &      |        AND         | A & B  |   A 와 B가 모두 True일때만 True   |
|     \|      |         OR         | A \| B |   A 와 B중 하나만 True여도 True   |
|      ^      |        XOR         | A ^ B  |       A 와 B가 다르면 True        |
|      ~      |        NOT         |  ~ A   |            A 비트 반전            |
|     <<      |  비트 왼쪽 시프트  | A << B |  A 비트를 B 만큼 왼쪽으로 시프트  |
|     >>      | 비트 오른쪽 시프트 | A >> B | A 비트를 B 만큼 오른쪽으로 시프트 |



### 이 연산자를 언제 쓰면 좋을까

- n번째 원소 표현 **1 << n**

- n번째 원소 존재여부 판단 **var & (1 << n)**
- n번째 원소 추가 **var | (1 << n)**

- n번째 원소 삭제 **var & ~(1 << n)**
- n번째 원소 토글 **var ^ (1 << n)**

P.S. 비트연산을 이용하여 집합을 표현할 수 있음 (Ex. BOJ 11723)



### 비트필드

비트가 모여 만들어진 구조체 (Ex. 11010010)



### 비트필드 + DP

일반적으로 비트필드를 DP 테이블의 인덱스로 사용



### 비트필드, DP를 이용하여 푸는 문제들 접근

1. 기본틀은 DFS로 완탐하는 코드작성 -> 여기서 시간복잡도를 어떻게 줄일 수 있을까?
2. **메모이제이션**을 위해 리턴하는식으로 코드 수정
3. 방문한 노드들을 비트단위로 저장한걸 visit (예를들어 1, 3번노드 방문하면 2진수로 00001010)
4. 이것을 dp[cur]에 저장 가능

```python
# BOJ 1311 할일정하기 1
# 단순 DFS 코드

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
visited = [False for i in range(N)]
ans = 9999999

def recur(cur, tot):
    global ans

    if cur == N:
        ans = min(ans, tot)
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        recur(cur + 1, tot + arr[cur][i])
        visited[i] = False

recur(0, 0)
print(ans)
```

``` python
# visited -> 방문했다 안했다 -> 1, 0으로 표현 할 수 있을것 같다.

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
# visited = [False for i in range(N)]
ans = 9999999

def recur(cur, tot, visit):
    global ans

    # if cur == N:
    if visit == (1 << N) - 1:
        ans = min(ans, tot)
        return

    for i in range(N):
        bit = 1 << i
        if visit & bit:
            continue
        # visited[i] = True
        visit |= bit
        recur(cur + 1, tot + arr[cur][i], visit)
        # visited[i] = False
        visit &= ~(1 << bit)

recur(0, 0, 0)
print(ans)
```

- 아직도 시간초과, why?
  - 문제의 주어진 조건 N = 20, 시간제한 1초
  - 재귀로 구현하므로 최대 재귀깊이 20, 시간복잡도 20! 까지 가겠구나.
  - DP, 메모이제이션으로 시간복잡도 최적화 필요



```python
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
# visited = [False for i in range(N)]
dp = [[9999999 for i in range(1 << N)] for j in range(30)]


def recur(cur, visit):

    # if cur == N:
    if visit == (1 << N) - 1: # 모든노드를 방문했다면
        return 0

    if dp[cur][visit] != 9999999:  # 메모이제이션 해놓은 값이 있다면?
        return dp[cur][visit]

    for i in range(N):  # 처음 저장하는 경우라면 모든 노드를 순회
        bit = 1 << i
        if visit & bit:  # 이미 방문한 노드라면 skip
            continue
        dp[cur][visit] = min(dp[cur][visit], recur(cur + 1, visit | bit) + arr[cur][i])

    return dp[cur][visit]


print(recur(0, 0))
```



- ##### 점화식 분석

```
dp[cur][visit] 은 현재위치(cur)에서 visit에 있는 노드들을 방문했고 저장되는 값은, 방문한 노드들을 지나면서 갱신한 값(최소비용)이 아니라, cur에서 앞으로 다른 노드들을 방문할 때의 최소비용이 저장된다.
(DP를 recursive하게 짜면 탑다운 방식임을 주의, Ex.피보나치)

예를들면 1, 2, 3, 4번 노드가 있다고 치자
dp[1][10110] 은 현재위치가 1번노드이며, 4, 2, 1번노드를 방문한 상태, 그럼 저장되는 값은?
-> 1, 2, 4번노드를 방문했을때의 최소비용이 아니라, 남은 노드인 3번노드를 방문할 때의 최소비용.

다른 예. 1, 2, 3, 4, 5, 6번 노드가 있다고 치자
dp[3][001010] 은 현재위치가 3번노드, 1, 3번노드를 방문한상태,
저장되는 값은 1, 3번노드를 방문했을때의 최소비용이 아니라, 남은노드인, 2, 4, 5, 6번 노드를 방문할 때의 최소비용.

fibo(6)이 8인것은 죽었다 깨어나도 불변하는 사실이므로 새로 구하지 않고 메모이제이션 하듯이
dp[cur][visit] 도 메모이제이션으로 시간복잡도 최적화 가능.
```

```
dp[cur][visit] = min(dp[cur][visit], recur(cur + 1, visit | bit) + arr[cur][i])

-> 난지금 cur에 있고 visit을 방문한 상태야, 이 상태에서 남은 노드들을 방문할때의 최소비용을 dp에 저장해.
```

```
if dp[cur][visit] != 9999999:  
    return dp[cur][visit]

-> 이미 구한 값이 있어? 새로 구하지말고 꺼내써. 어차피 cur에서 visit을 제외한 노드들은 매번 계산해도 같을 테니까
```

```
if visit == (1 << N) - 1:
        return 0
-> 왜 리턴 0?
모든 노드를 방문했으면 리턴하는 위치를 생각해보자.
dp[cur][visit] = min(dp[cur][visit], recur(cur + 1, visit | bit) + arr[cur][i])
점화식에서 0 이 리턴되었다면
dp[cur][visit] = min(dp[cur][visit], arr[cur][i])
이렇게 바뀜.
-> cur에서 남은 노드가 i밖에 없으면 cur에서 i로 가는 비용이 최소비용이 되니까 
```



### BOJ 2098 외판원 순회, 1311 할일정하기 코드 비교

```python
# 2098 외판원 순회 1
n = int(input())

INF = int(1e9)
dp = [[INF] * (1 << n) for _ in range(n)]


def dfs(x, visited):
    if visited == (1 << n) - 1:     # 모든 도시를 방문했다면
        if graph[x][0]:             # 출발점으로 가는 경로가 있을 때
            return graph[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF

    if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, n):           # 모든 도시를 탐방
        if not graph[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue

        # 점화식
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]


graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print(dfs(0, 1))
```

```python
# 1311 할 일 정하기 1

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
# visited = [False for i in range(N)]
dp = [[9999999 for i in range(1 << N)] for j in range(30)]


def recur(cur, visit):

    # if cur == N:
    if visit == (1 << N) - 1: # 모든노드를 방문했다면 
        return 0

    if dp[cur][visit] != 9999999:  # 메모이제이션 해놓은 값이 있다면?
        return dp[cur][visit]

    for i in range(N):  # 처음 저장하는 경우라면 모든 노드를 순회
        bit = 1 << i
        if visit & bit:  # 이미 방문한 노드라면 skip
            continue
        dp[cur][visit] = min(dp[cur][visit], recur(cur + 1, visit | bit) + arr[cur][i])

    return dp[cur][visit]


print(recur(0, 0))
```

- 공통점이 보인다
  - DP, 메모이제이션
  - visit을 비트필드로 대체하고 인덱스로 사용
  - 같은 점화식



```python
def fibo(n):
    if dp[n] != -1:
        return dp[n]
   	if n==1 or n==2:
        dp[n] = 1
        return dp[n]
    
    dp[n] = fibo(n-1)+fibo(n-2)
    return dp[n]
```






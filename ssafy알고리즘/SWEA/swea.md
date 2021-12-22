### 1232_사칙연산

```python
T = 10

def calc(v):
    if len(tree[v]) == 2:
        return tree[v][1]
    else:
        l = calc(tree[v][2])
        r = calc(tree[v][3])
        
        if tree[v][1] == '+': return l+r
        elif tree[v][1] == '-': return l-r
        elif tree[v][1] == '*': return l*r
        elif tree[v][1] == '/': return l/r


for tc in range(1,T+1):
    N = int(input())	# 정점의 개수
    tree = [0] * N+1
    
    for i in range(1,N+1):
        tmp = input().split()
        
        tree[int(tmp[0])] = tmp
        
        # 먼저 처리를 하고 가자
        if len(tmp) == 4:
            tree[int(tmp[0])][2] = int(tree[int(tmp[0])][2])
            tree[int(tmp[0])][3] = int(tree[int(tmp[0])][3])
        else:
            tree[int(tmp[0])][1] = int(tree[int(tmp[0])][1])
   
    print("#{} {}".format(tc,int(calc(1))))
    
######################################################################
# 나중에 처리하자
def calc(v):
    if len(tree[v]) == 2:
        return int(tree[v][1])
    else:
        l = calc(int(tree[v][2]))
        r = calc(int(tree[v][3]))
        
        if tree[v][1] == '+': return l+r
        elif tree[v][1] == '-': return l-r
        elif tree[v][1] == '*': return l*r
        elif tree[v][1] == '/': return l/r

for tc in range(1,T+1):
    N = int(input())	# 정점의 개수
    tree = [0] * N+1
    
    for i in range(1,N+1):
        tmp = input().split()
        
        tree[int(tmp[0])] = tmp
```



### 1949. 등산로 조성

```python
def dfs(G,v):
    if not visited[v]:
        visited[v] = 1
    for 
    	if not visited[w]:
            dfs(G,w)
    visited[v] = 0
```



### 1952. 수영장

```python
'''
min(1일 이용권, 한달 이용권)
dp사용

'''
```



### 10966. 물놀이

```python
'''
bfs(초음파가 퍼지는 모양으로)
땅에서 물을 찾자 -> 물(1)에서 땅(0)을 찾자!, 물(0),땅(999999)
'''
```



### 탈주범 검거

```python
'''
우 0 하 1 좌 2 상 3
타입1 : 상하좌우[1,1,1,1] [0,1,2,3]
타입2 : 상,하 [0,1,0,1] [1,3]
타입3 : 좌,우 [1,0,1,0] [0,2]
타입4 : 상,우 [1,0,0,1] [0,3]
타입5 : 하,우 [1,1,0,0] [0,1]
타입6 : 하,좌 [0,1,1,0] [1,2]
타입7 : 상,좌 [0,0,1,1] [2,3]

2->0 , 0->2
1->3 , 3->1 ===> (i+2)%4

bfs
'''
```


# Tree

### 순회방법

- 전위순회(preorder traversal) : VLR

  부모노드 방문 후, 자식노드를 좌,우 순서로 방문한다.

- 중위순회(inorder traversal) : LVR

  왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문한다.

- 후외순회(postorder traversal) : LRV

  자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다.



### 전위순회

현재 노드n 방문하여 처리 -> 현재 노드의 왼쪽 서브트리 -> 현재 노드의 오른쪽 서브트리

```python
def preorder_traverse(T):
    if T:
        visit(T)
        preorder_traverse(T.left)
        preorder_traverse(T.right)
```



### 중위순회

현재 노드의 왼쪽 서브트리 ->  현재 노드n 방문하여 처리 -> 현재 노드의 오른쪽 서브트리 

```python
def inorder_traverse(T):
    if T:
        inorder_traverse(T.left)
        visit(T)
        inorder_traverse(T.right)
```



### 후위순회

현재 노드의 왼쪽 서브트리 -> 현재 노드의 오른쪽 서브트리 -> 현재 노드n 방문하여 처리

```python
def postorder_traversal(T):
    if T:
        postorder_traversal(T.left)
        postorder_traversal(T.right)
        visit(T)
```



### 배열을 이용한 이진트리 표현

**노드번호의 성질**

노드번호가 i인 노드의 부모 노드 번호? floor(i/2)

노드번호가 i인 노드의 왼쪽 자식 노드 번호? 2* i

노드 번호가 i인 노드의 오른쪽 자식 노드 번호? 2*i+1

레벨 n(루트노드는 레벨 0, 노드 번호 1)의 노드 번호 시작 번호는? 2^n

**단점**

편향 이진 트리의 경우 메모리공간 낭비 발생, 노드 삭제 시 배열 변경이 어려워 비효율적



<연습문제-전위순회>

```python
def pre_order(n):
    if n:	# 유효한 정점이면
        print(n)
        pre_order(left[n])	# n의 왼쪽 자식으로 이동
        pre_order(right[n])


V = int(input())
edge = list(map(int,input().split()))
E = V - 1 # V개의 정점이 있는 트리의 간선 수
left = [0]*(V+1) # 부모를 인덱스로 자식번호 저장
right = [0]*(V+1)
for i in range(E):
    p,c = edge[i*2], edge[i*2+1]
    if left[p] == 0: # p의 왼쪽자식이 없으면
        left[p] = c
    else:			# 왼쪽 자식이 있으면 오른쪽 자식으로 저장
        right[p] = c

pre_order(1)        
```



### 이진 탐색 트리

#### 탐색 연산

- 루트에서 시작
- 탐색할 키 값 x를 루트 노드의 키 값과 비교한다.
  - 키 값 x = 루트 노드의 키 값 인 경우 : 원하는 원소를 찾았으므로 성공
  - 키 값 x < 루트 노드의 키 값 인 경우 : 루트노드의 왼쪽 서브트리에 대해서 탐색연산 수행
  - 키 값 x > 루트 노드의 키 값 인 경우 : 루트노드의 오른쪽 서브트리에 대해서 탐색연산 수행

#### 삽입 연산

탐색 실패한 위치에 삽입한다.

#### 삭제 연산

왼쪽 서브 트리에 가장 오른쪽 노드를 루트노드로 교체? 하는 느낌으로

#### 시간 복잡도

O(h) , h: BST의 깊이

O(log n) : 평균

O(n): 최악의 경우



**※ 힙(heap)** : 부모 > 자식, 완전 이진 트리 (부모번호 = 자식번호 // 2)

- 키값이 가장 큰 노드나, 가장작은 노드를 찾기에 유용한 자료구조

- 최소힙은 가장 작은 키값을 가진 노드가 항상 루트에 위치한다.
- 힙의 키를 우선순위로 활용하여 우선순위 큐를 구현할 수 있다.



```python
# 조상찾기
V = int(input())
edge = list(map(int,input().split()))
E = V - 1 # V개의 정점이 있는 트리의 간선 수
left = [0]*(V+1) # 부모를 인덱스로 자식번호 저장
right = [0]*(V+1)
par = [0]*(V+1) # 자식을 인덱스로 부모번호 저장

for i in range(E):
    p,c = edge[i*2], edge[i*2+1]
    if left[p] == 0: # p의 왼쪽자식이 없으면
        left[p] = c
    else:			# 왼쪽 자식이 있으면 오른쪽 자식으로 저장
        right[p] = c
    par[c] = p 	# (1) 조상을 찾는데 사용
    			# (2) root 찾기

c = 4 # 4의 조상 찾기
while par[c]:
    print(par[c])
    c = par[c]

# 부모가 없으면 root    
root = 1
while par[root]: # par[root] == 0 되면 while 종료 -> 그때 root
    root += 1
print(root)
```


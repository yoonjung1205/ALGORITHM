### 1219. 길 찾기

```python
for _ in range(1):
    tc, N = map(int, input().split())
    road = list(map(int,input().split()))
    
    # 1.홀짝
    # 2.2step
    # 3.2*
    for i in range(N):
        st = road[2*i]
        en = road[2*i+1]
    ######################################
    # 저장 방법
    # 1. ch1, ch2
    ch1 = [0] * 100
    ch2 = [0] * 100
    
    for i in range(N):
        if ch1[road[2*i]] == 0:
            ch1[road[2*i]] = road[2*i+1]
        else:
            ch2[road[2*i]] = road[2*i+1]
            
    # 2. 인접행렬 방식
    arr = [[0]*100 for _ in range(100)]
    for i in range(N):
        arr[road[2*i][road[2*i+1]]=1
            
    # 3. 인접리스트 방식
    adj_list = [[] for_ in range(100)]
    for i in range(N):
            adj_list[road[2*i]].append(road[2*i+1])
            
    visited = [0] * 100
    ans = 0
            
    stack = [0]
    
    while stack:
        curr = stack.pop()
            
        if curr == 99:
            ans = 1
            break
        # 방문하지 않았으면
        # 방문을 했으면 건너가
        if visited[curr]: continue
        visited[curr] = 1
            
        for w in adj_list[curr]:
            if not visited[w]:
            	stack.append(w)
            
    print('#{} {}'.format(tc, ans))   
```

재귀 이용

```python
def DFS(v):
    global ans
    if v==99:
        ans = 1
        return
    
	visited[v] = 1
    
    for w in range(100):
        if not vistited[w] and arr[v][w]:
            DFS(w)

for _ in range(1):
    tc, N = map(int, input().split())
    road = list(map(int,input().split()))
    
    arr = [[0]*100 for _ in range(100)]
    for i in range(N):
        arr[road[2*i][road[2*i+1]] = 1
            
    visited = [0] * 100
    ans = 0    
```



### 6485. 삼성시의 버스 노선

```python
T = int(input())

#1.모든 노선 체크
def bus_count(bus_stop):
    cnt = 0
    for i in range(N):
        if bus_route[i][0] <= bus_stop <= bus_route[i][1]:
            cnt += 1
    return cnt
for tc in range(1,T+1):
	N = int(input()) # 버스 노선 수
    
    bus_route = [] # 버스의 노선들을 저장해 놓을 리스트
    
    for i in range(N):
        A,B = map(int,input().split())
        bus_route.append((A,B))
	# 내가 확인하고 싶은 정류장의 개수        
    P = int(input())
    ans = [] # 버스 수를 저장해 놓을 리스트
    
    for i in range(P):
        C = int(input())
        ans.append(bus_count(C))
    print('#{}'.format(tc), end=' ')
    print(' '.join(map(str,ans)))
######################################################
#2. 정류장을 미리 계산 해보자
for tc in range(1,T+1):
	N = int(input()) # 버스 노선 수
    
    start = [0] * 5001	#출발 정류장
    end = [0] * 5001	#도착 정류장
    bus_stop = [0] * 5001 #계산한 버스 표시
    
    for i in range(N):
        A,B = map(int,input().split())
        start[A] += 1
        end[B] += 1
    for i in range(len(bus_stop)-1):
        bus_stop[i+1] = bus_stop[i] - end[i] + start[i+1]
    P = int(input())
    print('#{}'.format(tc),end=' ')
    for i in range(P):
        C = int(input()) # 우리가 확인하고 싶은 정류장 번호
        print(bus_stop[C], end=' ')
    print()
########################################################
#3. 미리계산
for tc in range(1,T+1):
	N = int(input()) # 버스 노선 수
    
    bus_stop = [0] * 5001
    
    for i in range(N):
        A,B = map(int,input().split())
        for j in range(A,B+1):
            bus_stop[j] += 1
            
    P = int(input())
    print('#{}'.format(tc),end=' ')
    for i in range(P):
        C = int(input()) # 우리가 확인하고 싶은 정류장 번호
        print(bus_stop[C], end=' ')
    print()
```



### 1859. 백만장자 프로젝트

```python
T = int(input())
#1. 순서대로 계산 (case 예시가 커지면 시간 오래걸림, 시간초과)
for tc in range(1,T+1):
    N = int(input())
    cost = list(map(int, input().split())) # 가격들 입력받음
    
    ans = 0
    
    for i in range(N-1): # 어차피 마지막날은 사도그만 안사도 그만
        amx_cost = cost[i]
        for j in range(i+1,N):
            if max_cost < cost[j]:
                max_cost = cost[j]
                
        if max_cost > cost[i]:
            ans += max_cost - cost[i] # 이익을 구하자!
########################################################            
#2. 사는게 이득인지 아닌지 확인 -> 1.보다는 빠르나 얘도 느려!
for tc in range(1,T+1):
    N = int(input())
    cost = list(map(int, input().split())) # 가격들 입력받음
    
    ans = 0
    # 사는게 이득인지 아닌지 체크
    is_sell = [False] * N
    for i in range(N-1):
        for j in range(i+1,N):
            if cost[i] < cost[j]:
                is_sell[i] = True
                break
                
    buy_cost = 0
    buy_cnt = 0
    
    for i in range(N):
        if is_sell[i]:
            buy_cost += cost[i]
            buy_cnt += 1
        else: 
            ans += (cost[i] * buy_cnt) - buy_cost #판매수익 - 
            buy_cost = 0
            buy_cnt = 0
########################################################
#3. 반대로 생각
for tc in range(1,T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    max_cost = cost[-1]
    result = 0
    for i in range(N-2,-1,-1):
        if cost[i] > max_cost:
            max_cost = cost[i]
        else:
            result += max_cost - cost[i]    
```



### 4408. 자기 방으로 돌아가기

```python
def div(num):
    return (int(num)+1)//2

for tc in range(1,T+1):
    N = int(input()) # 돌아갈 사람의 수
    students = [list(map(int,input().split())) for _ in range(N)]
    
    road = [0] * 201 # 복도 (방번호 대신 복도번호)
    for i in range(N):
        if students[i][0] > students[i][1]: #현재 방 > 돌아가야할 방
            students[i][0],students[i][1] = students[i][1],students[i][0]
        for j in range(students[i][0],students[i][1]+1):
            road[j] += 1
    print('#{} {}'.format(tc, max(road)))
```



### 1979. 어디에 단어가 들어갈 수 있을까

```python
#1.벽을 만났을때까지
#2.끝나기 전 K까지 -> 벽을 두른다...
for tc in range(1,T+1):
    N, K = map(int,input().split()) # N:2차원 리스트 키, K:내가 찾고 싶은 길이
    #띠를 두르자
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    puzzle.append([0]*(N+1))
    
    
    ans = 0
    
    for i in range(N+1):
      	# 행을 검사
        cnt_r = 0
        for j in range(N+1):
            if puzzle[i][j] == 1: # 흰색부분일때
                cnt_r += 1
            else:
                if cnt_r == K:
                    ans += 1
                cnt_r = 0
        # 끝까지 가서야 완성이 되는 경우
        #if cnt_r == K:
        #    ans += 1
    	# 열을 검사
        cnt_c = 0
        for j in range(N+1):
            if puzzle[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                	ans+= 1
                cnt_c = 0
        #if cnt_r == K:
        #    ans += 1       
```



### 5356. 의석이의 세로로 말해요

```python
# 허락맡고 가자 -> if문 사용
# 허락말고 용서를 구하자! -> try except 문
for tc in range(1,T+1):
    word = [0] * 5
    max_len = 0
    for i in range(5):
        word[i] = list(input()) # 값을 바꾸지 않으면 str그대로 해도된다!
        if len(word[i]) > max_len:
            max_len = len(word[i])
    print('#{}'.format(tc),end=' ')
    
    for i in range(max_len):
        for j in range(5):
            #1. 허락받고 쓰자
            #if len(word[j]) > i:
            #    print(word[j][i],end='')
            #2. 쓰고 용서구하기
            try:
                print(word[j][i],end='')
            except:
                pass
    print()
```



### 5432. 쇠막대기 자르기

```python
for tc in range(1,T+1):
    iron_bar = inpur()
    
    stack = []
    ans = 0
    
    for i in range(len(iron_bar)):
        if iron_bar[i]=='(':
            stack.append('(')
        else:
            stack.pop()
            if iron_bar[i-1]=='(': #레이저임
                ans += len(stack)
            else:
                ans += 1
####################################################          
for tc in range(1,T+1):
    iron_bar = inpur()
    
    cnt = 0
    ans = 0
    
    for i in range(len(iron_bar)):
        if iron_bar[i]=='(':
            cnt += 1
        else:
            cnt -= 1
            if iron_bar[i-1]=='(': #레이저임
                ans += cnt
            else:
                ans += 1
```



### 1974. 스도쿠 검증

```python
T = int(input())

def check()
	for i in range(9):
        row = [0] * 10
        col = [0] * 10
        
        for j in range(9):
            # 행을 검사
            num_row = sudoku[i][j]
            # 열을 검사
            num_col = sudoku[j][i]
            
            #이미 사용한 숫자라면 멈춰
            if row[num_row]: return 0
            if col[num_col]: return 0
            
        	row[num_row] = 1
            col[num_col] = 1
            ###########################
            #3x3 검사도 가능
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        num = sudoku[r][c]
                        # 중복된 숫자가 나오면 그만!
                        if square[num]: return 0
                        square[num] = 1
    return 1               
for tc in range(1,T+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    print('#{} {}'.format(tc,check()))
```



### 1961. 숫자 배열 회전

```python
# arr_180[i][j] = arr[N-1-i][N-1-j]
# arr_270[i][j] = arr[j][N-1-i]
```


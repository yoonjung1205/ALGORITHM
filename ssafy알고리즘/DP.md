# Memoization

이전에 계산한 값을 메모리에 저장 -> 다음 계산에 적용해서 빠르게 계산할 수 있음

계산시간을 theta(n) 으로 줄일 수 있다.

```python
def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]

def fibo2(n):
    if n>=2 and memo2[n]==0: # 아직 계산되지 않은 값이면
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]
n=50
memo2 = [0]*(n+1)
memo2[0] = 0
memo2[1] = 1
print(fibo2)
```



# DP(Dynamic Programming)

한 문제를 여러 개의 하위 문제로 나누어 푼 후, 결합하여 문제를 해결한다.  하위 문제의 정답을 저장한 후 이를 같은 하위 문제가 나왔을 때 다시 계산하지 않고 이미 저장된 정답을 활용하는 방법. 하위 문제가 많을 때 유용하게 사용 할 수 있다. 

DP를 사용할 수 있는 경우

- 큰 문제를 작은 문제로 나눌 수 있다.
- 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

다이나믹 프로그래밍 = 점화식?

#### 피보나치 수열

```python
def fibo(n):
    if n == 0:
        return 0
	if n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
```

fibo(10) = 55 은 쉽게 구해지지만... n이 더 커진다면 ?? 구하는데 오래걸릴것이다 ! (O(2^n))

이때 DP를 사용하면 계산량을 줄일 수 있습니다. -> **MEMOIZATION** 기법 활용 (O(N))

#### 피보나치 수열 DP

한 번은 저장된 값까지 계산을 해주고 이 후에 발생되는 동일한 계산은 저장된 배열에서 찾아올 수 있기 때문에 시간이 많이 절약됩니다.

``` python
# 수업시간에 배운 예(bottom-up방식 : 작은문제부터 차근차근 답을 도출한다.)
def fibo2(n):
    table[0] = 0
    table[1] = 1
    
    for i in range(2,n+1):
        table[i] = table[i-1]+table[i-2]
        
    return table[n]

n = int(input())
table = [0] * (n+1) # DP 테이블

print(fibo2(n))

# 다른 예(재귀사용, top-down방식 : 큰 문제를 해결하기 위해 작은 문제를 호출한다.)
def fibo3(n):
    if n == 1 or n == 2:
        return 1
    # 이미 계산한 것
    if table[n] != 0:
        return table[n]
    # 계산하지 않은 것
    table[n] = fibo3(n-1) + fibo3(n-2)
    return table[n]

print(fibo3(n))
```



#### 팩토리얼

```python
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
```

#### 팩토리얼 DP

```python
def fact(n):
    table[0] = 1
    
    for i in range(1,n+1):
        table[i] = i * table[i-1]
        
    return table[n]

n = int(input())
table = [0] * (n + 1)

print(fact(n))
```





규칙, 가짓수, 경우의 수 구하는 문제일 경우 dp 일 가능성 높음

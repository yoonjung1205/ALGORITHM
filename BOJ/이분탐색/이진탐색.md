이진탐색 + 매개변수 탐색

binary search + parametric search



이진탐색은 정렬된 배열에서 찾고자 하는 값의 존재여부나 정확한 위치를 찾는것

대충 이런 모양

```python
arr = [1, 2, 3, 4, 10, 20, 25, 30, 33, 37, 50]
n = int(input())

s = 0
e = len(arr) - 1
while s <= e:
    mid = (s + e) // 2

    if arr[mid] == n:
        print("찾음")
        exit()
    elif mid > n:
        e = mid - 1
    else:
        s = mid + 1
print("못찾음")
```

우리는 이런 이진탐색코드에 익숙해져 있다.



우리가 어려워하는 이진탐색 정확히말하면 매개변수탐색(parametric search)임

보통 코테에서 문제가 이진탐색으로 나온다면 거의 이진+매개변수탐색으로 나온다고 보면 된다.



매개변수탐색은 배열에서 조건에 만족하는 구간내에서 최댓값/최솟값을 찾는것

Ex)

[T,T,T,T,**T**,F,F,F,F,F,F,F,F]

[F,F,F,F,F,F,F,F,**T**,T,T,T,T,T,T,T,T]

T, F 변환구간은 한번만 존재해야 한다



이진탐색은 그 값이 있냐? 없냐? 였지만 

이것을 조건을 만족하냐? 안하냐?로 바꿔준다면

조건을 만족하는 구간내에서 정답이 될수 있는 값을 계속 땡겨주며 찾아주는것이다



공유기설치

s = 0

e = 9999999

1	2	4	8	9

거리 1일경우

v	v	v	v	v	5개	

거리 2일경우

v	x	v	v	x	3개

v	x	v	x    v

거리 3일경우

v	x	v	v	x	3개

v	x	v	x	v

거리 4일경우

v	x	x	v	x	2개

v	x	x	x	v



코드는 이진탐색과 비슷

```python
n, m = map(int, input().split())
arr = [int(input()) for i in range(n)]
arr.sort()

def check(x):
    cnt = 1
    prv = arr[0]

    for i in range(1, n):
        if arr[i] >= prv + x:
            cnt += 1
            prv = arr[i]

    return cnt >= m

s = 1
e = 1000000000
ans = 0
#최대값을 구하고싶다 [t,t,T,f,f ...]
while s <= e:
    mid = (s + e) // 2  # 공유기 사이의 거리가 mid,

    if check(mid):  # mid간격으로 설치했을 때 m개이상 설치가 되나?
        ans = mid
        s = mid + 1     #되면 s를 땡겨: 더나은값(더 최대가 있는지 찾아야해)
    else:
        e = mid - 1     #안되면 e를 땡겨

print(ans)
```






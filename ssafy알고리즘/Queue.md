# Queue

- 선입선출(First In First Out)
- 삽입 : enQueue, 삭제 : deQueue

```python
def enQueue(item):
    global rear
    if isFull() : print('Queue Full')
    else:
        rear += 1
        Q[rear] = item
def deQueue():
    if isEmpty() : print('Queue Empty')
    else:
        front += 1
        return Q[front]
    
def isEmpty():
    return front == rear
def Full():
    return rear == len(Q)-1
def Qpeek():
    if isEmpty(): print('Queue Empty')
    else: return Q[front+1]
```



원형 큐

- front = rear = 0
- front rear 위치가 마지막 인데스 가리킨 후, 다시 처음 인덱스 0으로 이동. 이를 위해 mod 연산자 사용

- 공백과 포화를 구분하기 위해, front 자리는 비워둔다(포화 : (rear+1)mod n = front)
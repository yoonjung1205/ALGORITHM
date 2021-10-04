t = int(input())

for _ in range(t):
    s = int(input())
    store = list(map(int,input().split()))
    store.sort()
    m = (store[0]+store[-1])//2
    result = (m - store[0])*2 + (store[-1] - m)*2

    print(result)
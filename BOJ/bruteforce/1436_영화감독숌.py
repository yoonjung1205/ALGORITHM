N = int(input())

arr = [0]*10000000
cnt = 0
for i in range(10000000):
    if '666' in str(i):
        cnt += 1
        arr[cnt] = i
        # print(arr[cnt])
print(arr[N])


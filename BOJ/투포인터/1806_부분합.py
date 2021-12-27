N, S = map(int,input().split())

arr = list(map(int, input().split()))

# print(arr)


l = []
total = 0
ans = 987654321
end = 0
for start in range(N):
    while end < N:
        if total >= S:
            break
        total += arr[end]
        l.append(arr[end])
        end += 1
    if ans > len(l) and total >= S:
        ans = len(l)
    total -= arr[start]
    if l:
        l.pop(0)

if ans == 987654321:
    print(0)
else:
    print(ans)
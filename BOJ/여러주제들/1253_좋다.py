N = int(input())
arr = list(map(int,input().split()))
visit = [0] * N
arr.sort()

cnt = 0
for i in range(len(arr)):
    start = 0
    end = len(arr) - 1

    while start < end:
        total = arr[start] + arr[end]
        if total == arr[i]:
            if end == i:
                end -= 1
            elif start == i:
                start += 1
            else:
                cnt += 1
                break
        elif total > arr[i]:
            end -= 1
            if end == i:
                end -= 1
            if start == i:
                start += 1
        else:
            start += 1
            if end == i:
                end -= 1
            if start == i:
                start += 1

print(cnt)
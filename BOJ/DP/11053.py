N = int(input())
arr = [0] + list(map(int,input().split()))

# 
temp = arr[1]
ans = 1
bin = 1
for i in range(2,len(arr)):
    if arr[i] > temp:
        ans += 1
        bin += 1
    elif arr[i] == temp:
        continue
    else:
        bin = 1


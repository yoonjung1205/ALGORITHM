N = int(input())
arr = list(map(int, input().split()))
odd = []    # 인덱스 1,3,5,7, ...
even = []   # 인덱스 0,2,4,8, ...

for i in range(N):
    if i % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

even.sort()
odd.sort()

if 1 in odd:
    print('NO')
    quit()

if len(even) > len(odd):
    for i in range(len(even)-1):
        if odd[i]-even[i] != 1:
            print('NO')
            quit()
    print('YES')

else:
    for i in range(len(even)):
        if odd[i]-even[i] != 1:
            print('NO')
            quit()
    print('YES')
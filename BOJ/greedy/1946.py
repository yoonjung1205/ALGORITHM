import sys

T = int(input())
for _ in range(T):
    num = int(input())
    tuple_list = [tuple(map(int,input().split()))for i in range(num)]
    tuple_list.sort(key = lambda x:x[0])
    
    cnt = 0
    for i in range(len(tuple_list)-1,0,-1):
        for j in range(i-1,-1,-1):
            if tuple_list[i][1] > tuple_list[j][1]:
                cnt += 1
                break

    print(len(tuple_list) - cnt)


import sys

T = int(input())
for _ in range(T):
    num = int(input())
    tuple_list = [tuple(map(int,sys.stdin.readline().split()))for i in range(num)]
    tuple_list.sort(key = lambda x:x[0])
    l = len(tuple_list)
    cnt = 1
    first = tuple_list[0][1]
    for i in range(1,l):
        if tuple_list[i][1] < first:
            cnt += 1
            first = tuple_list[i][1]

    print(cnt)
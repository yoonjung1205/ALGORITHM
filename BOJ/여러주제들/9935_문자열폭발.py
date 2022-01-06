arr = list(input())
bomb = list(input())
bomb_size = len(bomb)
idx = 0
cnt = 0

if len(arr) < bomb_size:
    arr = "".join(arr)
    print(arr)
    exit()

while idx < len(arr):
    if arr[idx] == bomb[0]:
        cnt = 0
        for i in range(bomb_size):
            if arr[idx+i] == bomb[i]:
                cnt += 1
                continue
            else:
                cnt = 0
                break
        if cnt == bomb_size:
            for j in range(bomb_size):
                arr.pop(idx)
                # print('pop: ',arr)

            idx -= bomb_size+1
    if idx < 0:
        idx = 0
    else:
        idx += 1


if arr:
    arr = "".join(arr)
    print(arr)
else:
    print('FRULA')
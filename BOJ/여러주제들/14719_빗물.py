H, W = map(int,input().split())
block = list(map(int, input().split()))
idx = block.index(max(block))
temp = block[0]
rain = 0
for i in range(1,idx+1):
    if block[i] < temp:
        rain += temp-block[i]
    else:
        temp = block[i]

temp2 = block[-1]
for i in range(W-1,idx,-1):
    if block[i] < temp2:
        rain += temp2-block[i]
    else:
        temp2 = block[i]

print(rain)
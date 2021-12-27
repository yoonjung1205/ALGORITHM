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

# 투포인터 사용(지슬)
# h, w = map(int, input().split())
# blocks_h = list(map(int, input().split()))
#
# l = 0
# r = w-1
#
# max_l = max_r = 0
# rainwater = 0
# while l < r:
#     max_l = max(max_l, blocks_h[l])
#     max_r = max(max_r, blocks_h[r])
#     if max_l < max_r:
#         rainwater += max_l - blocks_h[l]
#         l += 1
#     else:
#         rainwater += max_r - blocks_h[r]
#         r -= 1
#
# print(rainwater)
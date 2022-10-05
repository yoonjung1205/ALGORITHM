from collections import deque
n, w, L = map(int, input().split())
trucks = list(map(int,input().split()))
index = 0

total_weight = 0
time = 0
# bridge = deque([0]*w)
# while index < n:
#     # 다리 무게를 못이기면, 이길때까지 트럭반대편으로 운송
#     if total_weight + trucks[index] > L:
#         while total_weight + trucks[index] > L:
#             if bridge[0] == 0:
#                 bridge.rotate(-1)
#             else:
#                 out = bridge.popleft()
#                 total_weight -= out
#                 if len(bridge) < w:
#                     bridge.append(0)
#             if total_weight + trucks[index] > L:
#                 time += 1
#         bridge.append(trucks[index])
#         if len(bridge) > w:
#             bridge.popleft()
#         total_weight += trucks[index]
#         time += 1
#
#     else:
#         bridge.append(trucks[index])
#         if len(bridge) > w:
#             bridge.popleft()
#         total_weight += trucks[index]
#         time += 1
#
#     index += 1
# # print('여기서 bridge는', bridge)
# # print('여기서 bridge[0]는', bridge[0])
#
# # 모든 트럭 다싣고 다리건너기
# while bridge[0] == 0:
#     # bridge.rotate(-1)
#     bridge.popleft()
#     time += 1
#
# for i in bridge:
#     if i != 0:
#         # bridge.popleft()
#         time += 1
#     else:
#         break
bridge = [0] * w
while bridge:
    bridge_out = bridge.pop(0)
    total_weight -= bridge_out
    if trucks:
        if total_weight + trucks[0] <= L:
            truck = trucks.pop(0)
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)

    time += 1
print(time)
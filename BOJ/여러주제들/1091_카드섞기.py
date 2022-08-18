import copy
N = int(input())

# P = [2,0,1] 이면 0번째 카드는 2번플레이어에게 가야한다는 뜻
Player = list(map(int,input().split()))

# S = [1,2,0] 이면 0번째 카드는 1번째 위치로 이동
S = list(map(int,input().split()))
temp = list(range(0,N))
card = list(range(0,N))
mix_card = list(range(0,N))

result = 0
while True:
    # 해당 플레이어에 돌아갔는지 확인
    cnt = 0
    for i in range(N):
        if Player[mix_card[i]] == i % 3:
            cnt += 1
    if cnt == N:
        break

    # 섞기
    for i in range(N):
        mix_card[S[i]] = card[i]

    # 섞은 카드가 처음이랑 같다면, 해당 플레이어에게 카드 돌아갈수 없음
    if mix_card == temp:
        result = -1
        break
    card = copy.deepcopy(mix_card)
    result += 1
print(result)




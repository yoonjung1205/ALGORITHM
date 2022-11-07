N, X = map(int,input().split())
voice_limit = list(map(int,input().split()))
game = [X-1] * N

idx = 0
while True:
    game[idx] = game[idx-1] + 1
    if game[idx] > voice_limit[idx]:
        print(idx+1)
        break
    idx += 1
    if idx == len(game):
        idx = 0
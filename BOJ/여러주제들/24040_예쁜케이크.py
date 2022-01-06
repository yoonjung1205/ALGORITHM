T = int(input())
for _ in range(T):
    N = int(input())
    if N % 9 == 0 or (N+1) % 3 == 0:
        print('TAK')
    else:
        print('NIE')
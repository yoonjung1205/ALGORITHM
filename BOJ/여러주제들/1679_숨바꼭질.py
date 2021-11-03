N,K = map(int,input().split())

def search(N,K,cnt):
    global result
    if N == K:
        return cnt
    for x in [N-1, N+1, 2*N]:
        cnt += 1
        if x == N-1 and not visit[N-1]:
            N = N-1
            visit[N] = 1
            return search(N,K,cnt)
        elif x == N+1 and not visit[N+1]:
            N = N+1
            visit[N] = 1
            return search(N,K,cnt)
        elif x == 2*N and not visit[2*N]:
            N = 2*N
            visit[N] = 1
            return search(N,K,cnt)
visit= [0] * 100001
search(N,K,0)

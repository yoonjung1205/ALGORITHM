T = 1
while True:
    N = int(input())
    if N == 0:
        break

    manitto = {}
    visit = {}
    for i in range(N):
        me, you = map(str, input().split())
        manitto[me] = you
        visit[me] = 0


    cnt = 0
    def check(key,start, dictionary):
        global cnt
        visit[key] = 1
        if dictionary[key] == start:
            cnt += 1
            return
        return check(dictionary[key],start, dictionary)

    for k in manitto:
        start = k

        if not visit[k]:
            check(k,start,manitto)


    print(T, cnt)
    T += 1

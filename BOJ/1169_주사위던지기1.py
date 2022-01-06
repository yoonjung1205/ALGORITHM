# n,m = map(int,input().split())
#
# def dice1(cur):
#     if cur == n:
#         print(*arr)
#         return
#
#     for i in range(6):
#         arr[cur] = i+1
#         dice1(cur+1)
#
# def dice2(cur,start):
#     if cur == n:
#         print(*arr)
#         return
#
#     for i in range(start,7):
#         arr[cur] = i
#         dice2(cur+1,i)
#
# def dice3(cur):
#     if cur == n:
#         print(*arr)
#         return
#
#     for i in range(6):
#         if visit[i]:
#             continue
#         visit[i] = 1
#         arr[cur] = i+1
#         dice3(cur+1)
#         visit[i] = 0
#
#
# arr = [0]*n
# visit = [0]*6
# if m == 1:
#     dice1(0)
#
# if m == 2:
#     dice2(0,1)
#
# if m == 3:
#     dice3(0)




def solution(n, k, bulbs):
    bulbs = list(bulbs)
    idx = 0
    answer = 0
    if len(bulbs) % k != 0 or len(set(bulbs)) > k:
        answer = -1
    else:
        while 1:
            if bulbs[idx] != 'R':
                answer += 1
                for i in range(k):
                    if bulbs[idx+i] == 'R':
                        bulbs[idx+i] = 'G'
                    elif bulbs[idx+i] == 'G':
                        bulbs[idx+i] = 'B'
                    else:
                        bulbs[idx+i] = 'R'
                    # print(bulbs)
                idx = 0
            elif bulbs[idx] == 'R':
                idx += 1
            if len(set(bulbs)) == 1:
                break

    return answer

print(solution(4,2,"GBBG"))
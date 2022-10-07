# 시간초과 무조건 나는 코드
N = int(input())
tower = [100000000]+list(map(int, input().split()))
# answer = []
# for i in range(N-1,-1,-1):
#     flag = 0
#     for j in range(i,-1,-1):
#         if tower[i] < tower[j]:
#             answer.append(j+1)
#             flag = 1
#             break
#     if flag == 0:
#         answer.append(0)
# print(*answer[::-1])

# 모노톤 스택
# 대표적으로 '현재 값보다 작은(or 큰) 가장 근접한 요소'를 찾는 알고리즘의 문제로 사용됨
# (이것을 O(n)만에 풀 수있는 강력한 풀이법)
answer = []
answer.append(0)

for i in range(1,N+1):
    while tower[i] > tower[answer[-1]]:
        answer.pop()

    print(answer[-1], end=" ")
    answer.append(i)
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

# 0b~ : 이진수, int
# bin() : 이진수, str

# & : 모두 1이면 1
# | : 하나만 1이면 1
# ^ : 같으면 0, 다르면 1

# def add(x):
#     global s
#     s = s | (1 << x)
#
#
# def remove(x):
#     global s
#     s = s & ~(1 << x)
#
#
# def check(x):
#     global s
#     if s & (1 << x):
#         print(1)
#     else:
#         print(0)
#
# def toggle(x):
#     global s
#     s = s ^ (1 << x)
#
#
# def all():
#     for i in range(1,21):
#         add(i)
#
# def empty():
#     global s
#     s = 0
#
# cnt = int(input())
# s = 0
# # arr = [list(input().strip().split()) for _ in range(cnt)]
# # print(arr)
# for i in range(cnt):
#     # print('연산: ',arr[i])
#
#     temp = input().strip().split()
#     # print(temp)
#     if len(temp) == 1:
#         if temp[0] == 'all':
#             all()
#         elif temp[0] == 'empty':
#             empty()
#
#     else:
#         operate, num = temp
#         num = int(num)
#
#         if operate == 'add':
#             add(num)
#         elif operate == 'remove':
#             remove(num)
#         elif operate == 'check':
#             check(num)
#         elif operate == 'toggle':
#             toggle(num)
import sys
input = sys.stdin.readline

cnt = int(input())
s = 0

for i in range(cnt):
    temp = input().strip().split()
    if len(temp) == 1:
        if temp[0] == 'all':
            s = (1 << 20)-1
            print(s)
        elif temp[0] == 'empty':
            s = 0

    else:
        operate, num = temp
        num = int(num)-1    #이유를 모르겠네??

        if operate == 'add':
            s = s | (1 << num)
        elif operate == 'remove':
            s = s & ~(1 << num)
        elif operate == 'check':
            if s & (1 << num):
                print(1)
            else:
                print(0)
        elif operate == 'toggle':
            s = s ^ (1 << num)


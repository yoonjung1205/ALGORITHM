# input_list = map(int,input().split())
# input_list = list(input_list)
# chess_list = [1,1,2,2,2,8]

# result = []
# for i in range(len(input_list)):
#     result.append(chess_list[i]-input_list[i])
#     print(result[i],end=' ')

# while True:
#     n = input()
#     if int(n) == 0:
#         break
#     length = len(n) + 1
#     for i in range(len(n)):
#         if 2 <= int(n[i]) <= 9:
#             length += 3
#         elif int(n[i]) == 1:
#             length += 2
#         else:
#             length += 4
#     print(length)    

# my_list = ['-','\\','(','@', '?', '>', '&', '%','/']

# while True:
#     total = 0
#     n = input()
#     if n == '#':
#         break
#     for i in range(len(n)):
#         for j in range(len(my_list)):
#             if n[i] == '/':
#                 total += -1 * (8 ** (len(n)-i-1))
#             if n[i] == my_list[j]:
#                 total += j * (8 ** (len(n)-i-1))
#     print(total)
# while True:
#     s = input().lower()
#     if s == '#':
#         break
#     count = 0
#     v = 'aeiou'
#     for i in range(len(s)):
#         if s[i] in v:
#             count += 1
#     print(count)
# a = [int(input()) for i in range(9)]

# print(max(a))
# for i in range(len(a)):
#     if a[i] == max(a):
#         print(i+1)

# a = [int(input()) for i in range(9)]

# r = sum(a) - 100
# for i in range(0,9):
#     for j in range(i+1,9):
#         if a[i] + a[j] == r:
#             a[i] = 0
#             a[j] = 0
# a.sort()
# for i in a:
#     if i != 0:
#         print(i)

# N, K = input().split()
# N = int(N)
# K = int(K)
# my_list = [str(N*i) for i in range(1,K+1)]
# result = []
# for i in my_list:
#     result.append(int(i[::-1]))
# print(max(result))


# h,m = map(int, input().split())
# if m < 45:
#     if h == 0:
#         h = 24
#     print(h-1,(60+m)-45)
# else:
#     print(h,m-45)

N = int(input())
lis = []
for i in range(1,N+1):
    if N == i + sum(map(int,str(i))):
        print(i)
        lis.append(i)
        break
    if i == N:
        print(0)

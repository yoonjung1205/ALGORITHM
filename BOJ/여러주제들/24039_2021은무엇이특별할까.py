N = int(input())

# 약수 개수가 4개인거 찾고 조건에 맞추기위해 시행착오 겪는중
# for i in range(N+1,10001):
#     flag = 0
#     cnt = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             # print(j)
#             if 1 < j < 10 or 99 < j < i:
#                 flag = 1
#                 break
#             cnt += 1
#     if cnt == 4 and not flag:
#         print(i)
#         break

# 에라토스테네스 체 사용해서 풀어보기
import math
prime = list(range(10001))
for i in range(2,int(math.sqrt(10000))+1):
    if prime[i]:
        j = 2
        while i*j <= 10000:
            prime[i*j] = 0
            j += 1
r_prime = []
for i in range(len(prime)):
    if prime[i] and prime[i] != 1:
        r_prime.append(prime[i])
# print(r_prime)
for i in range(len(r_prime)-1):
    if r_prime[i] * r_prime[i+1] > N:
        print(r_prime[i] * r_prime[i+1])
        break


# import math
# prime = [1] * 10001
# for i in range(2,int(math.sqrt(10000))+1):
#     if prime[i]:
#         j = 2
#         while i*j <= 10000:
#             prime[i*j] = 0
#             j += 1
# r_prime = []
# for i in range(2,len(prime)):
#     if prime[i]:
#         r_prime.append(i)
# # print(r_prime)
# for i in range(len(r_prime)-1):
#     if r_prime[i] * r_prime[i+1] > N:
#         print(r_prime[i] * r_prime[i+1])
#         break


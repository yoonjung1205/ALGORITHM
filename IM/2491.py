from typing import AnyStr


N = int(input())
num = list(map(int,input().split()))

plus = [num[0]]
minus = [num[0]]
l = 1
for i in range(1,N):
    if plus and plus[-1] < num[i]:
        minus = []
        minus.append(num[i])
        plus.append(num[i])
        
    elif minus and minus[-1] > num[i]:
        plus = []
        plus.append(num[i])
        minus.append(num[i])
        
    elif plus[-1] == num[i] or minus[-1] == num[i]:
        plus.append(num[i])
        minus.append(num[i])
    if len(minus) > l:
        l = len(minus)
    if len(plus) > l:
        l = len(plus)

print(l)


'''
# 출처 : https://m.blog.naver.com/withsghong/222094651727
def check(nums):
    global ans
    cnt = 1
    for i in range(1,N):
        if nums[i-1] <= nums[i]:
            cnt += 1
        else:
            cnt = 1
        
        if ans < cnt:
            ans = cnt

N = int(input())
arr = list(map(int,input().split()))

ans = 1

check(arr)
check(arr[::-1])
print(ans)'''
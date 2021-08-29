s = int(input())

num = list(map(int,input().split()))
new = [1]
temp = 0
for i in range(1,s):
    new.insert(i-(num[i]),i+1)

print(*new) 
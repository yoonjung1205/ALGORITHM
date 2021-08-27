N,M = map(int,input().split())
J = int(input())
apple = [int(input()) for i in range(J)]
bucket_s = 1
bucket_e = M
move = 0
for i in range(len(apple)):
    if (apple[i] == bucket_s) or (apple[i] == bucket_e):
        continue
    if bucket_e < apple[i]:
        move += apple[i] - bucket_e
        bucket_e = apple[i]
        bucket_s = apple[i]-M+1
        
    elif  apple[i] < bucket_s:
        move += bucket_s - apple[i]
        bucket_s = apple[i]
        bucket_e = apple[i]+M-1
        
print(move)

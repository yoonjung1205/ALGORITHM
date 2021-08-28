N = int(input())

stick = [list(map(int,input().split())) for _ in range(N)]
print(stick)
stick.sort()
print(stick)
# x = 2 3 4 5 6 7 8  9 10 11 12 13 14 15
# y = 4   6       10                  8
#                 (max) 

'''x = [i for i in range(stick[0][0],stick[-1][0]+1)]
print(x)'''
x=[]
y=[]
for i in range(N):
    x.append(stick[i][0])
    y.append(stick[i][1])

print(x)
print(y)

stack_y = [y[0]]
for i in range(N):   
    if stack_y[-1] < y[i]:
        stack_y.append(y[i])
    if stack_y[-1] == max(y):
        stack_y.append(y[i+1])
print(stack_y)
    

    







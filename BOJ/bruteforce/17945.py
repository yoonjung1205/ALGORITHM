A,B = map(int,input().split())
for i in range(-1000,1000):
    if i ** 2 + (2*A*i) + B == 0:
        if A**2 == B:
            print(i)
        else:
            print(i,end=' ')
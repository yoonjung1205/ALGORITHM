# 개미 문제

w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())


#출처 : https://par3k.tistory.com/139

a = (p+t) // w
b = (q+t) // h

if a % 2 == 0:
    x = (p+t) % w
else:
    x = w - (p+t) % w

if b % 2 == 0:
    y = (q+t) % h
else:
    y = h - (q+t) % h

print(x,y)
'''T = int(input())

my_list = []
for i in range(T):
    my_list.append(int(input()))

is_prime = [1] * (10000 + 1)        
is_prime[1] = 0 
# 소수 저장
for j in range(2,10000+1):
        if j*j > 10000:
            break
        if not is_prime[j]:
            continue
        for k in range(j * j, 10000+1,j):
            is_prime[k] = 0

for i in range(T):    
    for m in range(my_list[i]//2,1,-1):
        if is_prime[my_list[i] - m] == 1 and is_prime[m] == 1:
            print(m,my_list[i]-m)
            break'''

T = int(input())

my_list = []
for i in range(T):
    my_list.append(int(input()))
is_prime = [1] * (my_list[-1] + 1)        
is_prime[0] = 0
is_prime[1] = 0 
for j in range(2,my_list[-1]+1):
    if j*j > my_list[-1]:
        break
    if not is_prime[j]:
        continue
    for k in range(j * j, my_list[-1]+1,j):
        is_prime[k] = 0

for i in range(T):
    prime_list = []
    for l in range(2,my_list[i]+1):
        if is_prime[l]:
            prime_list.append(l)
    
    for m in range(len(prime_list)-1,-1,-1):
        flag = 0
        for n in range(m,len(prime_list)):
            if prime_list[m] + prime_list[n] == my_list[i]:
                print(prime_list[m], my_list[i]-prime_list[m])
                flag = 1
                break       
        if flag == 1:
            break

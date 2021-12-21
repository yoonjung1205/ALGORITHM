# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서
# 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
def switch_change(num):
    if switch[num] == 1:
        switch[num] = 0
    else:
        switch[num] = 1

def male(num):
    for i in range(1,len(switch)):
        if i % num == 0:
            switch_change(i)

def female(num):
    for i in range(switch_num//2):
        if num - i < 0 or num + i > switch_num:
            break
        if switch[num-i] == switch[num+i]:
            switch_change(num-i)
            switch_change(num+i)
        else:
            break


switch_num = int(input())
switch = [-1] + list(map(int, input().split()))
student_num = int(input())

for i in range(student_num):
    gender, number = map(int, input().split())
    if gender == 1:
        male(number)
    else:
        switch_change(number)
        female(number)

for i in range(1,switch_num+1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()



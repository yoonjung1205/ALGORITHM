def light(a):
    global result
    for i in range(0,len(led),a):
        if led[i] == 'Y':
            led[i] = 'N'

        else:
            led[i] = 'Y'

    result += 1

    return led

led = list(input())
led.insert(0, 0)


# 최소횟수, 정답
result = 0

for i in range(1,len(led)):
    if led[i] == 'N':
        continue
    else:
        led = light(i)

    if led == 'N'*len(led):
        break

print(result)
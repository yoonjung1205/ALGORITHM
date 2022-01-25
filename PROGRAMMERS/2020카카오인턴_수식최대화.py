from itertools import permutations


def op_cal(num1, num2, ope):
    if ope == '*':
        return num1 * num2
    if ope == '+':
        return num1 + num2
    if ope == '-':
        return num1 - num2


def solution(expression):
    answer = 0
    ope = ['*', '+', '-']
    ope = list(permutations(ope, 3))
    # print(ope)

    num = list(expression)
    arr = []
    tmp = ''
    # print(list(num))
    for w in range(len(num)):
        if num[w] not in '*-+':
            tmp += num[w]
        else:
            arr.append(tmp)
            arr.append(num[w])
            tmp = ''
        if w == len(num) - 1:
            arr.append(tmp)

    result = []
    for op in ope:
        arr2 = arr[:]
        for o in op:
            s = []
            while arr2:
                p = arr2.pop(0)
                if p != o:
                    s.append(p)
                else:
                    s.append(op_cal(int(s.pop()), int(arr2.pop(0)), o))
            arr2 = s
        result.append(abs(int(s[0])))

    answer = max(result)

    return answer

solution("100-200*300-500+20")
def solution(topping):
    answer = 0
    # topping 길이가 2일때는 무조건 1가지(예외잡기)
    if len(topping) == 2:
        return 1

    # 간단하지만, 시간초과 무조건!
    # for i in range(1,len(topping)):
    #     if len(set(topping[:i])) == len(set(topping[i:])):
    #         answer += 1

    cheolsu = [0] * 10001
    brother = [0] * 10001

    # 철수
    cheolsu[topping[0]] = 1
    c_topping_num = 1

    # 동생
    b_topping_num = 0
    for j in range(1, len(topping)):
        if brother[topping[j]] == 0:
            b_topping_num += 1
        brother[topping[j]] += 1

    # print(c_topping_num,b_topping_num)

    for i in range(1, len(topping)):
        if cheolsu[topping[i]] == 0:
            c_topping_num += 1
        cheolsu[topping[i]] += 1
        brother[topping[i]] -= 1

        if brother[topping[i]] == 0:
            b_topping_num -= 1

        if c_topping_num == b_topping_num:
            answer += 1

    return answer
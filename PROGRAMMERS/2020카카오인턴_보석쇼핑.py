def solution(gems):
    check = {}
    for gem in gems:
        check[gem] = 0
    check[gems[0]] = 1
    s = 0
    e = 0
    num_gems = 1
    min_s = 0
    min_e = len(gems) - 1

    def check_values(dic):
        for i in dic.values():
            if i <= 0:
                return False
        return True

    while e < len(gems) and s < len(gems):
        # if check_values(check):
        #     if min_e - min_s > e - s:
        #         min_e = e
        #         min_s = s
        #     check[gems[s]] -= 1
        #     s += 1
        # else:
        #     e += 1
        #     if e < len(gems):
        #         check[gems[e]] += 1

        if num_gems == len(check):
            if min_e - min_s > e - s:
                min_e = e
                min_s = s
            check[gems[s]] -= 1
            if check[gems[s]] == 0:
                num_gems -= 1
            s += 1
        else:
            e += 1
            if e < len(gems):
                check[gems[e]] += 1
                if check[gems[e]] == 1:
                    num_gems += 1

    answer = [min_s + 1, min_e + 1]
    return answer
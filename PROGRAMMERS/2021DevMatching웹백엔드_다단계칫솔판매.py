def solution(enroll, referral, seller, amount):
    answer = []
    # {나 : 나의 부모}
    parents = {}
    income = {}
    for i in range(len(enroll)):
        parents[enroll[i]] = referral[i]
        income[enroll[i]] = 0

    # print(parents)

    # sell = {}
    # for i in range(len(seller)):
    #     sell[seller[i]] = amount[i] * 100

    def check_parents(name, my_money, give_money):

        # print(name, my_money, give_money)
        # print(income[name])
        income[name] += my_money
        if parents[name] != '-':

            if give_money < 1:
                # income[name] += my_money
                return
            return check_parents(parents[name], give_money - give_money // 10, give_money // 10)

    for i in range(len(seller)):
        check_parents(seller[i], amount[i] * 100 - (amount[i] * 100) // 10, (amount[i] * 100) // 10)

    for v in income.values():
        answer.append(v)

    return answer
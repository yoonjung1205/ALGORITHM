# def solution(user_id, banned_id):
#     answer = 0
#     hubo_id = [[] * (len(banned_id) + 1)]
#     banned_index = 0
#
#     while banned_index < len(banned_id):
#         user_index = 0
#         while user_index < len(user_id):
#             flag = 0
#             if len(user_id[user_index]) == len(banned_id[banned_index]):  # user_id랑 banned_id 길이가 같을때만 비교
#                 for i in range(len(banned_id[banned_index])):  # banned_id 항목 한개를 순회
#                     if banned_id[banned_index][i] == user_id[user_index][i] or banned_id[banned_index][i] == '*':
#                         if flag == 0:
#                             hubo_id[banned_index].append(user_id[user_index])
#                             flag = 1
#                         else:
#                             continue
#                     else:
#                         if hubo_id[banned_index]:
#                             hubo_id[banned_index].pop()
#                             break
#                         else:
#                             continue
#                     print(hubo_id)
#             user_index += 1
#         banned_index += 1
#     # print(hubo_id)
#
#     return answer


def solution(user_id, banned_id):
    answer = []
    hubo_id = [[] for _ in range(len(banned_id))]
    result = [[]]
    banned_index = 0

    while banned_index < len(banned_id):
        user_index = 0
        hubo = []
        while user_index < len(user_id):

            if len(user_id[user_index]) == len(banned_id[banned_index]):  # user_id랑 banned_id 길이가 같을때만 비교
                flag = 0
                for i in range(len(banned_id[banned_index])):  # banned_id 항목 한개를 순회
                    if banned_id[banned_index][i] == user_id[user_index][i] or banned_id[banned_index][i] == '*':
                        continue
                    elif banned_id[banned_index][i] != user_id[user_index][i]:
                        flag = 1
                        break
                if flag == 0:
                    for r in result:
                        if user_id[user_index] not in r:
                            hubo.append(r + [user_id[user_index]])
            user_index += 1
        result = hubo
        print(result)
        banned_index += 1

    for h in result:
        if set(h) not in answer:
            answer.append(set(h))

    print(answer)

    return answer
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])
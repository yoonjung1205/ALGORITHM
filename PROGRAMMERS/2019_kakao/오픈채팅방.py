def solution(record):
    answer = []
    name_result = {}
    status_result = []

    for info in record:
        if 'Leave' in info:
            status,user_id = info.split()
            status_result.append([status,user_id])
        else:
            status, user_id, name = info.split()
            status_result.append([status,user_id])
            name_result[user_id] = name
            
    print(status_result)
    print(name_result)

    for i in range(len(status_result)):
        if status_result[i][0] =="Enter":
            answer.append(name_result[status_result[i][1]] + "님이 들어왔습니다.")
        elif status_result[i][0] =="Leave":
            answer.append(name_result[status_result[i][1]] + "님이 나갔습니다.")
    return answer


# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# record = ["Enter uid1234 Muzi","Leave uid1234","Enter abc1234 Prodo","Change abc1234 Apeach","Enter uid1234 Ryan","Enter Ryan Ryan"]
record = ["Enter uid0606 Gimoi", "Enter uid4567 Prodo", "Leave uid0606", "Enter uid1234 Prodo", "Change uid1234 OhYeah"]

print(solution(record))
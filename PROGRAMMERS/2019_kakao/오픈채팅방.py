def solution(record):
    answer = []
    name_result = {}
    status_result = []
    total_status = ''
    for info in record:
        if 'Leave' in info:
            status,user_id = info.split()
        else: status, user_id, name = info.split()
        status_result.append([status,user_id])
        name_result[user_id] = name
    print(status_result)
    print(name_result)
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)
import math


def solution(fees, records):
    standard_time = fees[0]
    standard_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]
    answer = []
    in_infos = []
    out_infos = []
    car_info = {}
    for record in records:  # 입출차 기록 저장
        temp = record.split()
        if temp[2] == 'IN':
            in_infos.append([temp[1], temp[0]])
        else:
            out_infos.append([temp[1], temp[0]])
    in_infos.sort()
    out_infos.sort()
    print(in_infos)
    print('--------------')
    print(out_infos)

    while in_infos:
        index = 0
        if not out_infos or in_infos[index][0] != out_infos[index][0]:  # 출차기록이 전혀 없거나, 짝이 안맞는 경우
            out_time = 23 * 60 + 59
            in_time = int(in_infos[index][1][:2]) * 60 + int(in_infos[index][1][3:])
            time = out_time - in_time
            car_num = in_infos.pop(index)  # 차번호 정보가 필요해서 저장([0000, 06:00])

        elif in_infos[index][0] == out_infos[index][0]:  # 입출차 기록 짝이 맞는 경우
            out_time = int(out_infos[index][1][:2]) * 60 + int(out_infos[index][1][3:])
            in_time = int(in_infos[index][1][:2]) * 60 + int(in_infos[index][1][3:])
            time = out_time - in_time
            out_infos.pop(index)
            car_num = in_infos.pop(index)

        if car_num[0] in car_info:
            car_info[car_num[0]] += time
        else:
            car_info[car_num[0]] = time

        index += 1

    print(car_info)
    for v in car_info.values():
        if v <= standard_time:
            answer.append(standard_fee)
        else:
            answer.append(standard_fee + math.ceil((v - standard_time) / per_time) * per_fee)

    return answer
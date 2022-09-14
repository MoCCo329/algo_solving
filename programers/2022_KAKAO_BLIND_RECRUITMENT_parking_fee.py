# 주차 요금 계산 2022 KAKAO BLIND RECRUITMENT  2022-09-14


import math


def solution(fees, records):
    cars_dict = dict()
    for record in records:
        time, car, status = record[:5], int(record[6:10]), record[11:]
        time = int(time[:2]) * 60 + int(time[3:])

        if status == 'IN':
            if not cars_dict.get(car, 0):
                cars_dict[car] = [0, time]
            else:
                cars_dict[car][1] = time
        else:
            cars_dict[car][0] += time - cars_dict[car][1]
            cars_dict[car][1] = 0

    ans = []
    for car, tot in cars_dict.items():
        if tot[1] or not tot[0]:
            tot[0] += 23 * 60 + 59 - tot[1]
            tot[1] = 0
        fee = fees[1] if tot[0] <= fees[0] else fees[1] + math.ceil((tot[0] - fees[0]) / fees[2]) * fees[3]
        ans.append((car, fee))

    ans.sort()
    ans = [ans[i][1] for i in range(len(ans))]

    return ans
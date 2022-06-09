# [1차] 다트 게임 2018 KAKAO BLIND RECRUITMENT 2022-06-09


def solution(dartResult):
    idx = 0
    score = []
    multi = {"S": 1, "D": 2, "T": 3}
    L = len(dartResult)

    for _ in range(3):
        if dartResult[idx + 1] == "0":
            temp = 10
            idx += 2
        else:
            temp = int(dartResult[idx])
            idx += 1

        temp = temp ** multi[dartResult[idx]]
        idx += 1

        if idx < L and dartResult[idx] == "*":
            if score:
                score[-1] = score[-1] * 2
            score.append(temp * 2)
            idx += 1
        elif idx < L and dartResult[idx] == "#":
            score.append(-temp)
            idx += 1
        else:
            score.append(temp)

    return sum(score)
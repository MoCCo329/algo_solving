# [1차] 압축 2018 KAKAO BLIND RECRUITMENT  2022-06-11


def solution(msg):
    answer = [0]
    dic = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14,
           "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
    rear = 26
    
    N = len(msg)
    i = 0
    temp = ""
    while i < N:
        temp = temp + msg[i]
        chk = dic.get(temp, 0)
        if chk:
            i += 1
            answer[-1] = chk
        else:
            dic[temp] = rear + 1
            temp = ""
            if i < N:
                answer.append(chk)
            rear += 1
    
    # print(dic)
    return answer
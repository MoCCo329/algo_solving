# [1차] 뉴스 클러스터링 2018 KAKAO BLIND RECRUITMENT 2022-09-07


def solution(str1, str2):
    str1_filt = []
    str2_filt = []

    for i in range(len(str1) - 1):
        temp = str1[i:i + 2]
        if temp.isalpha():
            str1_filt.append(temp.lower())
    for i in range(len(str2) - 1):
        temp = str2[i:i + 2]
        if temp.isalpha():
            str2_filt.append(temp.lower())

    intersect1 = dict()
    intersect2 = dict()
    for cha in str1_filt:
        if cha in str2_filt:
            if intersect1.get(cha, 0):
                intersect1[cha] += 1
            else:
                intersect1[cha] = 1
    for cha in str2_filt:
        if cha in str1_filt:
            if intersect2.get(cha, 0):
                intersect2[cha] += 1
            else:
                intersect2[cha] = 1

    intersect = 0
    for key in intersect1:
        intersect += min(intersect1[key], intersect2[key])
    union = len(str1_filt) + len(str2_filt) - intersect

    if not union:
        ans = 65536
    else:
        ans = intersect / union * 65536

    return int(ans)
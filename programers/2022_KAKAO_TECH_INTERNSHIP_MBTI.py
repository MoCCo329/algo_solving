# 성격 유형 검사하기 2022 KAKAO TECH INTERNSHIP  2022-09-05


def solution(survey, choices):
    char_sum = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    char_type = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]

    for i in range(len(survey)):
        res = int(choices[i])
        if choices[i] <= 3:
            char_sum[survey[i][0]] += 4 - choices[i]
        elif choices[i] >= 5:
            char_sum[survey[i][1]] += choices[i] - 4

    ans = []
    for front, back in char_type:
        if char_sum[front] >= char_sum[back]:
            ans.append(front)
        else:
            ans.append(back)
    return ''.join(ans)
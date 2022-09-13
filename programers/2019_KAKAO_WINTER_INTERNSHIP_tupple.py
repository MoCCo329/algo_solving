# 튜플. 2019 카카오 개발자 겨울 인턴십  2022-09-14


def solution(s):
    L = len(s)
    i = 1
    arr = []
    while i < L - 1:
        temp = []
        if s[i] == '{':
            i += 1
            temp_str = ''
            while s[i] != '}':
                if s[i] == ',':
                    temp.append(int(temp_str))
                    temp_str = ''
                else:
                    temp_str += s[i]
                i += 1
            temp.append(int(temp_str))
            arr.append(temp)
        i += 1
    arr.sort(key=lambda x: len(x))

    ans = []
    for ar in arr:
        if not ans:
            ans = ar
            continue

        for a in ar:
            if a not in ans:
                ans.append(a)

    return ans
# [3차] 방금그곡 2018 KAKAO BLIND RECRUITMENT  2022-09-12


def solution(m, musicinfos):
    def code_split(code):
        i = 0
        L = len(code)
        res = []

        while i < L:
            if i + 1 < L and code[i + 1] == '#':
                res.append(code[i:i + 2])
                i += 2
            else:
                res.append(code[i])
                i += 1

        return res

    ans = []
    for i in range(len(musicinfos)):
        start, end, name, code = musicinfos[i].split(',')
        time = 60 * (int(end[:2]) - int(start[:2]) - 1) + (int(end[3:]) + 60 - int(start[3:]))

        code = code_split(code)
        all_code = code * (time // len(code)) + code[:(time % len(code))]
        all_code = '|'.join(all_code) + '|'
        m = code_split(m)
        all_m = '|'.join(m) + '|'

        if all_m in all_code:
            ans.append((-time, i, name))

    ans.sort()
    if ans:
        return ans[0][2]
    else:
        return '(None)'
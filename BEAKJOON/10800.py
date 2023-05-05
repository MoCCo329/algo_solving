# 10800. 컬러볼  2023-05-06


import sys
input = sys.stdin.readline


def find(c, s):  # c 컬러 s 사이즈보다 작은 idx 찾기
    temp = color_dict[c]
    l, r = 0, len(temp) - 1

    while l <= r:
        m = (l + r) // 2

        if temp[m] < s:
            l = m + 1
        else:
            r = m - 1

    return l


N = int(input())
balls = [list(map(int, input().split())) for _ in range(N)]
color_dict = {}
sum_color_dict = {}
sum_arr = [0] * 2001

for c, s in balls:
    if color_dict.get(c, -1) == -1: color_dict[c] = []

    color_dict[c].append(s)
    sum_arr[s] += s

for i in range(1, 2001):
    sum_arr[i] += sum_arr[i - 1]
for key in color_dict.keys():
    color_dict[key].sort()
    temp = color_dict[key]
    sum_color_dict[key] = [0]
    for i in range(len(temp)):
        sum_color_dict[key].append(sum_color_dict[key][-1] + temp[i])

for c, s in balls:
    tot = sum_arr[s - 1]
    idx = find(c, s)

    same_color = sum_color_dict[c][idx]

    print(tot - same_color)
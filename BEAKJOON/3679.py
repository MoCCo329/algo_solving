# 3679. 단순 다각형  2023-06-04


import sys


def comp(dot):
    if dot[1] == pivot[1]: return -sys.maxsize
    return -(dot[0] - pivot[0]) / (dot[1] - pivot[1])


T = int(input())
for tc in range(T):
    iterator = map(int, input().split())
    N = next(iterator)
    dots = []
    for i in range(N): dots.append((next(iterator), next(iterator), i))

    dots.sort(key=lambda x: (x[1], x[0]))
    pivot = dots.pop(0)
    dots.sort(key=comp)

    i = N - 3
    last_decline = comp(dots[-1])
    while comp(dots[i]) == last_decline:
        i -= 1

    print(pivot[2], end=" ")
    for i in range(i + 1):
        print(dots[i][2], end=" ")
    for i in range(N - 2, i, -1):
        print(dots[i][2], end=" ")
    print()
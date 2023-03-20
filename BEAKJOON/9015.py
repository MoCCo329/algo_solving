# 9015. 정사각형  2023-03-20


import sys
input = sys.stdin.readline


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dot_hs = set()
    ans = 0

    for _ in range(N):
        x, y = map(int, input().split())
        dot_hs.add((x, y))

    for x1, y1 in dot_hs:
        for x2, y2 in dot_hs:
            if x1 == x2 and y1 == y2: continue

            a, b = x2 - x1, y2 - y1

            if (x1 - b, y1 + a) in dot_hs and (x2 - b, y2 + a) in dot_hs:
                ans = max(ans, a ** 2 + b ** 2)
            if (x1 + b, y1 - a) in dot_hs and (x2 + b, y2 - a) in dot_hs:
                ans = max(ans, a ** 2 + b ** 2)

    print(ans)
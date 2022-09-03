# 9466. 텀 프로젝트  2022-09-03


import sys


T = int(input())
for _ in range(T):
    N = int(input())
    uf = [0] + list(map(int, sys.stdin.readline().split()))

    v = [0] * (N + 1)
    ans = N
    for i in range(1, N + 1):
        if v[i]: continue

        path = []
        while True:
            v[i] = 1
            path.append(i)
            i = uf[i]

            if v[i]:
                if i in path:
                    ans -= len(path) - path.index(i)
                break

    print(ans)
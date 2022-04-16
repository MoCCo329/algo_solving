# 14890. 경사로 2022-04-16


def t(line, N, L):
    i = 0
    v = [0] * N
    while i < N - 1:
        temp = line[i] - line[i + 1]
        if temp == 0:
            i += 1
            continue
        else:
            if abs(temp) > 1:
                return 0

            if temp == 1:
                if i + L >= N:
                    return 0
                k = 2
                v[i + 1] = 1
                for _ in range(L - 1):
                    if line[i + 1] != line[i + k]:
                        return 0
                    v[i + k] = 1
                    k += 1
                i += L
            elif temp == -1:
                if i - L + 1 < 0 or v[i] == 1:
                    return 0
                k = 1
                for _ in range(L - 1):
                    if line[i] != line[i - k] or v[i - k] == 1:
                        return 0
                    k += 1
                i += 1
    return 1


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    if t(arr[i], N, L):
        ans += 1
    if t([line[i] for line in arr], N, L):
        ans += 1

print(ans)
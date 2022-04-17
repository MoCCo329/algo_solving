# 15684. 사다리 조작 2022-04-16


def dfs(cnt, k, L):
    global ans

    if cnt >= ans:
        return

    for i in range(N):
        if i != test(i):
            break
    else:
        if ans > cnt:
            ans = cnt
        return

    for i in range(k, L):
        b, a = v[i]
        if b != N - 1 and Ladders[b][a] == 0 and Ladders[b + 1][a] == 0:
            Ladders[b][a] = + 1
            Ladders[b + 1][a] = - 1
            dfs(cnt + 1, i + 1, L)
            Ladders[b][a] = 0
            Ladders[b + 1][a] = 0


def test(i):
    state = 0
    while state < H:
        if Ladders[i][state] == - 1:
            i -= 1
        elif Ladders[i][state] == + 1:
            i += 1
        state += 1
    return i


N, M, H = map(int, input().split())
Ladders = [[0] * H for _ in range(N)]
v = [[i, j] for i in range(N - 1) for j in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    Ladders[b - 1][a - 1] = + 1
    Ladders[b][a - 1] = - 1
    v.remove([b - 1, a - 1])

L = len(v)
ans = 4
dfs(0, 0, L)
if ans == 4:
    print(-1)
else:
    print(ans)
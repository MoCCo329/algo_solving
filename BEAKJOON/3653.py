# 3653. 영화 수집  2023-03-04


def find(s, e):
    ans = 0
    while s <= e:
        if s % 2 == 1:
            ans += st[s]
            s += 1
        if e % 2 == 0:
            ans += st[e]
            e -= 1
        s //= 2
        e //= 2

    return ans


def update(i, x):
    st[i] = x
    i //= 2
    while i > 0:
        st[i] = st[i * 2] + st[i * 2 + 1]
        i //= 2


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    k = 1
    while k < N + M: k <<= 1

    end_idx = k + N - 1
    get_idx = [k + N - 1 - i for i in range(N)]

    st = [0] * (k << 1)
    for i in range(N): st[k + i] = 1
    for i in range(k - 1, 0, -1): st[i] = st[i * 2] + st[i * 2 + 1]

    iterator = map(int, input().split())
    for _ in range(M):
        a = next(iterator)
        s = get_idx[a - 1]
        print(find(s, end_idx) - 1, end=" ")

        end_idx += 1
        get_idx[a - 1] = end_idx
        update(s, 0)
        update(end_idx, 1)
    print()




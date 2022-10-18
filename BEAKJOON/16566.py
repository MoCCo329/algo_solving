# 16566. 카드 게임  2022-10-18


def find(x):
    if uf[x] == x:
        return x

    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):  # y에 x 붙이기
    X = find(x)
    Y = find(y)
    uf[X] = Y


def search(x):
    s, e = 0, M - 1

    while s <= e:
        m = (s + e) // 2
        if m_list[m] > x:
            e = m - 1
        else:
            s = m + 1
    return s


N, M, K = map(int, input().split())
m_list = list(map(int, input().split()))
k_list = list(map(int, input().split()))
m_list.sort()
uf = [i for i in range(M + 1)]

for k in k_list:
    card_i = search(k)
    print(m_list[find(card_i)])
    union(card_i, find(card_i) + 1)
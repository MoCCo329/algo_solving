# 4195. 친구 네트워크  2023-05-23


import sys
input = sys.stdin.readline


def find(a):
    if uf[a] == a: return a

    uf[a] = find(uf[a])
    return uf[a]


def union(a, b):  # a, b는 조상으로만 들어온다
    if a == b: return
    if uf_cnt[a] > uf_cnt[b]:
        a, b = b, a

    uf[b] = a
    uf_cnt[a] += uf_cnt[b]


for tc in range(int(input())):
    F = int(input())
    uf = [i for i in range(F * 2)]
    uf_cnt = [1] * (F * 2)
    idx = 0
    names = {}

    for _ in range(F):
        a, b = input().split()
        if a not in names:
            names[a] = idx
            idx += 1
        if b not in names:
            names[b] = idx
            idx += 1

        a_idx = names[a]
        b_idx = names[b]
        A, B = find(a_idx), find(b_idx)
        union(A, B)
        print(max(uf_cnt[A], uf_cnt[B]))
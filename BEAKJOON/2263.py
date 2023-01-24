# 2263. 트리의 순회  2023-01-24


import sys
sys.setrecursionlimit(100000)


def get_pre(in_s, in_e, post_s, post_e):
    if in_s > in_e or post_s > post_e: return

    print(post_order[post_e], end=" ")

    L = 0
    while in_s < in_e and in_order[in_e - L] != post_order[post_e]:
        L += 1

    get_pre(in_s, in_e - L - 1, post_s, post_e - L - 1)
    get_pre(in_e - L + 1, in_e, post_e - L, post_e - 1)

N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
get_pre(0, N - 1, 0, N - 1)
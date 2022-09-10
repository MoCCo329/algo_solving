# 1629. 곱셈  2022-09-10


def find(k):
    if memo_dict.get(k, -1) != -1:
        return memo_dict[k] % c

    if k % 2:
        memo_dict[k] = find(k - 1) * a % c
    else:
        memo_dict[k] = find(k / 2) ** 2 % c
    return memo_dict[k]


a, b, c = map(int, input().split())
memo_dict = { 1: a % c }

print(find(b))
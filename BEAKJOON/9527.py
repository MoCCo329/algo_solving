# 9527. 1의 개수 세기  2023-01-23


def count_one(n):  # n 까지 2진법으로 나타냈을 때 1이 나온 횟수
    n += 1
    L = len(format(n, 'b'))
    cnt = 0

    for l in range(L):
        div, mod = divmod(n, 1 << (l + 1))

        cnt += div * (1 << l)
        cnt += max(0, mod - (1 << l))
    return cnt

a, b = map(int, input().split())
print(count_one(b) - count_one(a - 1))
# 11444. 피보나치 수  2023-06-05


def fibo(n):
    if memo.get(n, -1) != -1: return memo[n]

    if n % 2 == 0:
        temp1, temp2 = fibo((n >> 1) - 1), fibo(n >> 1)
        memo[n] = ((2 * temp1 + temp2) % D) * temp2 % D
    else:
        temp1, temp2 = fibo((n >> 1) + 1), fibo(n >> 1)
        memo[n] = ((temp1 ** 2 % D) + (temp2 ** 2 % D)) % D

    return memo[n]


memo = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}
D = 1000000007

print(fibo(int(input())))
# 1234. 크리스마스 트리  2023-03-30


def factorial(n):
    L = len(factorial_memo)
    if L > n:
        return factorial_memo[n]

    for i in range(L, n + 1):
        factorial_memo.append(factorial_memo[-1] * i)

    return factorial_memo[n]


def DFS(l, r, g, b, m):
    global ans

    if l == N + 1:
        ans += m
        return

    temp = l // 3
    if l % 3 == 0 and temp <= r and temp <= g and temp <= b:
        DFS(l + 1, r - temp, g - temp, b - temp, m * factorial(l) // (factorial(temp) ** 3))

    temp = l // 2
    if l % 2 == 0:
        if temp <= r and temp <= g:
            DFS(l + 1, r - temp, g - temp, b, m * factorial(l) // (factorial(temp) ** 2))
        if temp <= r and temp <= b:
            DFS(l + 1, r - temp, g, b - temp, m * factorial(l) // (factorial(temp) ** 2))
        if temp <= g and temp <= b:
            DFS(l + 1, r, g - temp, b - temp, m * factorial(l) // (factorial(temp) ** 2))

    if l <= r:
        DFS(l + 1, r - l, g, b, m)
    if l <= g:
        DFS(l + 1, r, g - l, b, m)
    if l <= b:
        DFS(l + 1, r, g, b - l, m)


N, R, G, B = map(int, input().split())
ans = 0
factorial_memo = [1, 1, 2, 6, 24, 120]

DFS(1, R, G, B, 1)

print(ans)
# 1914. 하노이 탑  2023-04-06


def dfs(f, t, N):
    if N == 1:
        print(f, t)
        return

    other = 6 - f - t
    dfs(f, other, N - 1)
    print(f, t)
    dfs(other, t, N - 1)


N = int(input())
print(pow(2, N) - 1)
if N <= 20:
    dfs(1, 3, N)
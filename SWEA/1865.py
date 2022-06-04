# 1865. 동철이의 일 분배 2022-06-02


def dfs(k, N, pro):
    global ans

    if k == N:
        if pro > ans:
            ans = pro
    elif pro <= ans:
        return
    else:
        for i in range(N):
            if v[i] == 0:
                v[i] = 1
                dfs(k + 1, N, pro * arr[k][i])
                v[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(lambda x: int(x) * 0.01, input().split())) for _ in range(N)]
    v = [0] * N
    ans = 0
    dfs(0, N, 1)
    print(f'#{tc} {round(ans * 100, 6):.6f}')
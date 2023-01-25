# 16991 외판원 순회3  2023-01-25


def TSP(i, v):
    if v == END: return adj_mat[i][0]
    if dp[i][v] != 0: return dp[i][v]

    dp[i][v] = INF
    for j in range(N):
        if v & (1 << j): continue

        temp = TSP(j, v | (1 << j))
        dp[i][v] = min(dp[i][v], temp + adj_mat[i][j])

    return dp[i][v]


N = int(input())
adj_mat = [[0] * N for _ in range(N)]
nodes = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]
END = (1 << N) - 1
INF = 5000 * N

for i in range(N):
    for j in range(N):
        if i == j: continue

        temp = pow(pow(nodes[i][0] - nodes[j][0], 2) + pow(nodes[i][1] - nodes[j][1], 2), 0.5)
        adj_mat[i][j] = temp
        adj_mat[j][i] = temp

print(TSP(0, 1))
# 2098. 외판원 순회  2023-01-25


def TSP(i, v):
    # i 도시에서 부터 출발해 v 에 마킹안된 도시들을 탐험하고 출발지(0)로 돌아오는 최소비용.
    # 즉 모두 마킹됐으면 출발지(0) 로 돌아가기만 하면 된다.

    if v == END:
        if adj_mat[i][0] == 0: return INF
        return adj_mat[i][0]

    if dp[i][v] != 0: return dp[i][v]

    dp[i][v] = INF
    for j in range(N):  # 방문한 도시를 제외하고 다음 도시를 추가
        if adj_mat[i][j] == 0 or v & (1 << j): continue

        temp = TSP(j, v | (1 << j))  # j 도시를 포함한 경로를 탐험
        dp[i][v] = min(dp[i][v], adj_mat[i][j] + temp)

    return dp[i][v]


N = int(input())
adj_mat = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]
END = (1 << N) - 1
INF = 1000000 * N

print(TSP(0, 1))
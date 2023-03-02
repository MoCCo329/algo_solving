# 1102. 발전소  2023-03-03


def TSP(v, cnt):
    if cnt >= END:
        return 0

    if dp[v] != -1:
        if dp[v] == INF:
            return -1
        else:
            return dp[v]

    dp[v] = INF
    for i in range(N):
        if not (v & (1 << i)): continue
        for j in range(N):
            if v & (1 << j): continue

            temp = TSP(v | (1 << j), cnt + 1)
            if temp == -1: continue

            dp[v] = min(dp[v], temp + adj_matrix[i][j])

    if dp[v] == INF: return -1
    else: return dp[v]


N = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]
poss = input()
END = int(input())
dp = [-1] * (1 << N)
INF = 576

cnt = 0
v = 0
for i in range(N):
    if poss[i] == "Y":
        cnt += 1
        v += 1 << i

print(TSP(v, cnt))
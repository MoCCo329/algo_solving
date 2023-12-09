# 1208. 부분수열의 합2  2023-12-10


def dfs(t, k, cnt):
    global N, S, HALF, ans

    if (t and k == HALF) or (not t and k == N):
        if t:
            if cnt not in sum_map:
                sum_map[cnt] = 0
            sum_map[cnt] += 1
        else:
            if S - cnt in sum_map:
                ans += sum_map[S - cnt]
        return

    dfs(t, k + 1, cnt)
    dfs(t, k + 1, cnt + seq[k])


N, S = map(int, input().split())
HALF = N // 2
seq = list(map(int, input().split()))
sum_map = {}
ans = 0

dfs(True, 0, 0)
dfs(False, HALF, 0)

if S == 0:
    ans -= 1

print(ans)
# 15686. 치킨 배달 2022-04-17


def dfs(now, end, k, L):  # 현재 고른 수, 골라야 하는 개수, 진행된 chic 인덱스, chic 길이
    global ans
    if now == end:
        result = 0
        for house in houses:
            temp_ans = 10000
            for i in v:
                temp_dist = abs(chic[i][0] - house[0]) + abs(chic[i][1] - house[1])
                if temp_dist < temp_ans:
                    temp_ans = temp_dist
            result += temp_ans
        if ans > result:
            ans = result
        return

    if L - k < end - now:
        return
    else:
        for i in range(k, L - (end - now) + 1):
            v[now] = i
            dfs(now + 1, end, i + 1, L)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

houses = []
chic = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append([i, j])
        elif arr[i][j] == 2:
            chic.append([i, j])

L = len(chic)
ans = 10000
for end in range(1, M + 1):
    v = [0] * M
    dfs(0, end, 0, L)

print(ans)
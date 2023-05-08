# 광물 캐기.  2023-05-08


def dfs(k, N, tired):
    global ans, pick, tireds

    if tired >= ans:
        return

    if k >= N or sum(pick) == 0:
        ans = min(ans, tired)
        return

    for i in range(3):
        if pick[i] == 0: continue

        pick[i] -= 1
        dfs(k + 5, N, tired + tireds[k // 5][i])
        pick[i] += 1


def solution(picks, minerals):
    global ans, pick, tireds

    tireds = [[0] * 3 for _ in range((len(minerals) + 4) // 5)]
    pick = picks

    for i in range(len(minerals)):
        idx = i // 5
        if minerals[i] == "diamond":
            tireds[idx][0] += 1
            tireds[idx][1] += 5
            tireds[idx][2] += 25
        elif minerals[i] == "iron":
            tireds[idx][0] += 1
            tireds[idx][1] += 1
            tireds[idx][2] += 5
        else:
            tireds[idx][0] += 1
            tireds[idx][1] += 1
            tireds[idx][2] += 1

    ans = 751
    dfs(0, len(minerals), 0)

    return ans
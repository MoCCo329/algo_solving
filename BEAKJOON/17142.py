# 17142. 연구소 3 2022-04-26


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = -1
chk = N * N

viruses = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            viruses.append((i, j))
            arr[i][j] = -1
            chk -= 1
        elif arr[i][j] == 1:
            chk -= 1

if chk == 0:
    print(0)
    exit(0)
L = len(viruses)

V = [0] * K
def dfs(i, cnt, K):  # 현재 idx, 고른 개수, 골라야하는 개수
    global ans
    if cnt == K:
        newArr = [arr[i][::] for i in range(N)]
        q = []
        tempChk = 0
        for v in V:
            q.append((viruses[v][0], viruses[v][1]))
            newArr[viruses[v][0]][viruses[v][1]] = 1
        while q:
            if chk - tempChk == 0:
                break
            vi, vj = q.pop(0)
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni, nj = vi + di, vj + dj
                if 0 <= ni < N and 0 <= nj < N and (newArr[ni][nj] == 0 or newArr[ni][nj] == -1):
                    if newArr[ni][nj] != -1:
                        tempChk += 1
                    newArr[ni][nj] = newArr[vi][vj] + 1
                    q.append((ni, nj))

        if chk - tempChk == 0:
            tempAns = newArr[vi][vj]
        else:
            return

        if ans != -1:
            if ans > tempAns:
                ans = tempAns
        else:
            ans = tempAns

    elif L - i < K - cnt:
        return
    else:
        for j in range(i, L):
            V[cnt] = j
            dfs(j + 1, cnt + 1, K)

dfs(0, 0, K)
print(ans)
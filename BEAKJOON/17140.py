# 17140. 이차원 배열과 연산 2022-04-26


n, m, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

n, m = n - 1, m - 1
N, M = 3, 3
ans = 0
while not (0 <= n < N and 0 <= m < M and arr[n][m] == K) and ans <= 100:
    ans += 1
    if N >= M:
        maxM = 0
        for i in range(N):
            counts = [[i, 0] for i in range(101)]
            for j in range(M):
                counts[arr[i][j]][1] += 1
            arr[i] = []
            tempM = 0
            counts.sort(key=lambda x: (x[1], x[0]))
            for k in range(101):
                if counts[k][1] and counts[k][0] != 0:
                    arr[i] += [counts[k][0], counts[k][1]]
                    tempM += 2
            if tempM > maxM:
                maxM = tempM
        for i in range(N):
            arr[i] += [0] * max((maxM - len(arr[i])), (3 - len(arr[i])))
        M = maxM

    else:
        maxN = 0
        temp = [[] for _ in range(M)]
        for j in range(M):
            counts = [[i, 0] for i in range(101)]
            for i in range(N):
                counts[arr[i][j]][1] += 1
            tempN = 0
            counts.sort(key=lambda x: (x[1], x[0]))
            for k in range(1, 101):
                if counts[k][1] and counts[k][0] != 0:
                    temp[j] += [counts[k][0], counts[k][1]]
                    tempN += 2
            if tempN > maxN:
                maxN = tempN
        for j in range(M):
            temp[j] += [0] * max((maxN - len(temp[j])), (3 - len(temp[j])))
        N = maxN
        arr = [[temp[j][i] for j in range(M)] for i in range(N)]

if ans >= 101:
    print(-1)
else:
    print(ans)
# 17143. 낚시왕 2022-04-24


N, M, K = map(int, input().split())  # 격자크기 N, M, 상어 수 K
sharks = [list(map(int, input().split())) for _ in range(K)]  # N, M, s, d, z 순으로 저장 d 는 1부터 위, 아래, 오른쪽, 왼쪽
ans = 0
fisher = 0

while fisher < M and K:
    # 낚시꾼 이동
    fisher += 1
    kill = -1
    for i in range(K):
        if sharks[i][1] == fisher:
            if kill != -1:
                if sharks[kill][0] > sharks[i][0]:
                    kill = i
            else:
                kill = i
    if kill != -1:
        ans += sharks[kill][4]
        sharks.pop(kill)
        K -= 1

    # 상어 이동 및 없애기
    for i in range(K):
        n, m, s, d, z = sharks[i]
        if d == 1:
            if n - s >= 1:
                sharks[i][0] = n - s
            else:
                s = s - n + 1
                if (s // (N - 1)) % 2 == 0:
                    sharks[i][0] = (s % (N - 1)) + 1
                    sharks[i][3] = 2
                else:
                    sharks[i][0] = N - (s % (N - 1))
        elif d == 2:
            if N - n >= s:
                sharks[i][0] = n + s
            else:
                s = s - (N - n)
                if (s // (N - 1)) % 2 == 0:
                    sharks[i][0] = N - (s % (N - 1))
                    sharks[i][3] = 1
                else:
                    sharks[i][0] = (s % (N - 1)) + 1
        elif d == 3:
            if M - m >= s:
                sharks[i][1] = m + s
            else:
                s = s - (M - m)
                if (s // (M - 1)) % 2 == 0:
                    sharks[i][1] = M - (s % (M - 1))
                    sharks[i][3] = 4
                else:
                    sharks[i][1] = (s % (M - 1)) + 1
        elif d == 4:
            if m - s >= 1:
                sharks[i][1] = m - s
            else:
                s = s - m + 1
                if (s // (M - 1)) % 2 == 0:
                    sharks[i][1] = (s % (M - 1)) + 1
                    sharks[i][3] = 3
                else:
                    sharks[i][1] = M - (s % (M - 1))

    sharks.sort(key=lambda x:(x[0], x[1], -x[4]))
    i = 1
    while i < K:
        if sharks[i - 1][0] == sharks[i][0] and sharks[i - 1][1] == sharks[i][1]:
            sharks.pop(i)
            K -= 1
        else:
            i += 1

print(ans)
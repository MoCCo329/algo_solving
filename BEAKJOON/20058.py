# 20058. 마법사 상어와 파이어스톰  2022-10-13


N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2 ** N)]
turn = list(map(int, input().split()))

for t in turn:
    # 돌리기
    L = 2 ** t
    for i in range(2 ** N // L):
        for j in range(2 ** N // L):
            for k in range(L // 2):
                temp = arr[i * L + k][j * L + k:j * L + L - k]  # 상변 임시저장
                for l in range(1, L - (2 * k)):  # 좌변으로 상변 덮기
                    arr[i * L + k][j * L + k + l] = arr[i * L + L - 1 - k - l][j * L + k]
                for l in range(1, L - (2 * k)):  # 하변으로 좌변 덮기
                    arr[i * L + L - 1 - k - l][j * L + k] = arr[i * L + L - 1 - k][j * L + L - 1 - k - l]
                for l in range(1, L - (2 * k)):  # 우변으로 하변 덮기
                    arr[i * L + L - 1 - k][j * L + L - 1 - k - l] = arr[i * L + k + l][j * L + L - 1 - k]
                for l in range(L - (2 * k)):  # 상변으로 우변 덮기
                    arr[i * L + k + l][j * L + L - 1 - k] = temp[l]

    # 얼음 줄이기
    new_arr = [arr[i][::] for i in range(2 ** N)]
    for i in range(2 ** N):
        for j in range(2 ** N):
            cnt = 0
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and arr[ni][nj]:
                    cnt += 1
            if cnt < 3 and arr[i][j]:
                new_arr[i][j] -= 1
    arr = [new_arr[i][::] for i in range(2 ** N)]

# 정답 구하기
new_arr = [[0] * (2 ** N) for _ in range(2 ** N)]
ans1 = 0
ans2 = 0
for i in range(2 ** N):
    for j in range(2 ** N):
        ans1 += arr[i][j]
        if new_arr[i][j] or not arr[i][j]: continue
        q = [(i, j)]
        temp_ans = 1
        new_arr[i][j] = 1
        while q:
            ii, jj = q.pop(0)
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = ii + di, jj + dj
                if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and arr[ni][nj] and not new_arr[ni][nj]:
                    q.append((ni, nj))
                    temp_ans += 1
                    new_arr[ni][nj] = 1
        if ans2 < temp_ans:
            ans2 = temp_ans

print(ans1, ans2, sep='\n')
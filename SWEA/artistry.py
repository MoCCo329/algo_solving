# 삼성 SW 역량테스트 2022 상반기 오전 2번문제. 예술성  2022-10-14


def cal_score():
    s = [0]  # 해당 그룹의 크기와 다른 그룹과의 변 개수 저장
    v = [[0] * N for _ in range(N)]  # 방문 그룹 표시
    n = [0]  # 해당 그룹번호의 숫자
    group = 0
    for i in range(N):
        for j in range(N):
            if v[i][j]: continue
            group += 1
            s.append([0] * group)
            v[i][j] = group
            n.append(arr[i][j])

            cnt = 1
            q = [(i, j)]
            while q:
                ii, jj = q.pop(0)
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = ii + di, jj + dj
                    if not 0 <= ni < N or not 0 <= nj < N: continue
                    if arr[ni][nj] == arr[i][j] and not v[ni][nj]:
                        v[ni][nj] = group
                        cnt += 1
                        q.append((ni, nj))
                    elif arr[ni][nj] != arr[i][j] and v[ni][nj]:
                        s[group][v[ni][nj]] += 1
            s[group][0] = cnt

    result = 0
    for i in range(2, group + 1):
        for j in range(1, i):
            if not s[i][j]: continue
            result += (s[i][0] + s[j][0]) * n[i] * n[j] * s[i][j]
    return result


def rotate():
    # 십자가
    temp = [arr[l][L] for l in range(L)]  # 윗변 저장
    for l in range(L):
        arr[l][L] = arr[L][N - 1 - l]
        arr[L][N - 1 - l] = arr[N - 1 - l][L]
        arr[N - 1 - l][L] = arr[L][l]
        arr[L][l] = temp[l]
    
    # 정사각형
    for i in [0, L + 1]:
        for j in [0, L + 1]:
            temp = []
            for k in range(L):
                temp.append([arr[i + L - 1 - l][j + k] for l in range(L)])
            for k in range(L):
                for l in range(L):
                    arr[i + k][j + l] = temp[k][l]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
L = N // 2
ans = cal_score()
for _ in range(3):
    # 회전
    rotate()

    # 점수 계산
    ans += cal_score()

print(ans)
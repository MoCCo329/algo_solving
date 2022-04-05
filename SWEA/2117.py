# 2117. 홈 방범 서비스 2022-04-05

# def f(i, j, k):
#     cnt = 0
#     for ni in range(N):
#         for nj in range(N):
#             if arr[ni][nj] == 1 and abs(i - ni) + abs(j - nj) < k:
#                 cnt += 1
#     if 2 * k**2 - 2 * k + 1 <= cnt * M:
#         return cnt
#     else:
#         return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = []
#
#     for i in range(N):
#         for j in range(N):
#             k = 1
#             while k <= N+1:
#                 ans += [f(i, j, k)]
#                 k += 1
#
#     print(f'#{tc} {max(ans)}')


def f(i, j, k):
    global ans
    cnt = 0
    for hi, hj in house:
        if abs(hi - i) + abs(hj - j) < k:
            cnt += 1
    if 2 * k**2 - 2 * k + 1 <= cnt * M:
        if ans < cnt:
            ans = cnt
    return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    house = []
    ans = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                house.append((i, j))

    for i in range(N):
        for j in range(N):
            for k in range(2 * N - 1):
                f(i, j, k)

    print(f'#{tc} {ans}')
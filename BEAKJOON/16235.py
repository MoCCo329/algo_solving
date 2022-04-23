# 16235. 나무 재태크 2022-04-23


from collections import deque

N, M, K = map(int, input().split())
A = [list(map(lambda x: [int(x), 5], input().split())) for _ in range(N)]
arr = [[deque()] * N for _ in range(N)]
for _ in range(M):
    i, j, year = map(int, input().split())
    arr[i - 1][j - 1] = deque([year])

ans = M
for _ in range(K):
    spread = deque()
    for i in range(N):
        for j in range(N):
            tree = deque()
            plus = 0
            for year in arr[i][j]:
                if A[i][j][1] >= year:
                    tree.append(year + 1)
                    A[i][j][1] -= year
                    if (year + 1) % 5 == 0:
                        spread.append([i, j])
                else:
                    plus += year // 2
                    ans -= 1
            arr[i][j] = tree
            A[i][j][1] += plus

    for i, j in spread:
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj].appendleft(1)
                ans += 1

    for i in range(N):
        for j in range(N):
            A[i][j][1] += A[i][j][0]

print(ans)


# 시간초과가 나서 deque를 사용했는데, 그냥 A리스트를 둘로 나누고, spread 리스트가 아닌 배열을 한번 더 순회해서 번식하고,
# ans도 배열을 한번 더 순회해서 구한 답안은 훨씬 빠르게 되었다... 어설프게 최적화하려 하지말고 그냥 푸는게 더 빠른것 같다.
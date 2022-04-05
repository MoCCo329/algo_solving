# 5648. 원자 소멸 시뮬레이션 2022-04-05

d = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3: (1, 0)}

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(arr)):
        arr[i][0] *= 2
        arr[i][1] *= 2
    ans = 0

    for _ in range(4002):
        for i in range(len(arr)):
            di, dj = d[arr[i][2]]
            arr[i][0] += di
            arr[i][1] += dj

        ext, temp = set(), set()
        for i in range(len(arr)):
            ci, cj = arr[i][0], arr[i][1]
            if (ci, cj) in temp:
                ext.add((ci, cj))
            temp.add((ci, cj))

        for i in range(len(arr) - 1, -1, -1):
            if (arr[i][0], arr[i][1]) in ext:
                ans += arr[i][3]
                arr.pop(i)

    print(f'#{tc} {ans}')
# 9328. 열쇠  2022-09-01


def dfs(i, j):  # key를 만나면 key_dict에 담고 저장했던 gate 위치를 다시 탐색, 이후 .으로 변경후 계속 탐색, 열 수 있는 gate도 마찬가지
    global ans

    v[i][j] = 1
    now = arr[i][j]
    if now == '$':
        arr[i][j] = '.'
        ans += 1
    elif 97 <= ord(now) <= 122:  # key 인 경우
        arr[i][j] = '.'
        if keys.get(now, 0):
            pass
        else:
            keys[now] = 1
            if gates.get(now.upper(), 0):
                while gates.get(now.upper(), 0):
                    gi, gj = gates[now.upper()].pop(0)
                    arr[gi][gj] = '.'
                    dfs(gi, gj)
    elif 65 <= ord(now) <= 90:  # gate 인 경우
        if keys.get(now.lower(), 0):
            arr[i][j] = '.'
        else:
            if gates.get(now, 0):
                gates[now].append((i, j))
            else:
                gates[now] = [(i, j)]
            return

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 1 <= ni < N - 1 and 1 <= nj < M - 1 and arr[ni][nj] != '*' and v[ni][nj] == 0:
            dfs(ni, nj)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]  # $은 문서, . 은 이동가능, 대문자는 문, 소문자는 열쇠
    keys = list(input())

    if keys[0] == '0':
        keys = dict()
    else:
        key_dict = dict()
        for key in keys:
            key_dict[key] = 1
        keys = key_dict

    # 처음 가능한 구역들 탐색
    gates = dict()
    v = [[0] * M for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if (i == 0 or i == N - 1 or j == 0 or j == M - 1) and arr[i][j] != '*' and v[i][j] == 0:
                v[i][j] = 1
                dfs(i, j)

    print(ans)
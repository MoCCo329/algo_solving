# 16234. 인구 이동 2022-04-23


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]

ans = 0
while True:
    U = [[1, 1]]
    cnt = 1
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                q = [(i, j)]
                U.append([1, arr[i][j]])
                v[i][j] = cnt
                while q:
                    ii, jj = q.pop(0)
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ni, nj = ii + di, jj + dj
                        if 0 <= ni < N and 0 <= nj < N and L <= abs(arr[ii][jj] - arr[ni][nj]) <= R and v[ni][nj] == 0:
                            q.append((ni, nj))
                            U[cnt][0] += 1
                            U[cnt][1] += arr[ni][nj]
                            v[ni][nj] = cnt
                if U[cnt][0] != 1:
                    cnt += 1
                else:
                    U.pop()
                    v[i][j] = 0

    l = len(U)
    if l == 1:
        break
    else:
        ans += 1
        for i in range(1, l):
            U[i] = U[i][1] // U[i][0]

    for i in range(N):
        for j in range(N):
            cnt = v[i][j]
            if cnt != 0:
                arr[i][j] = U[cnt]
                v[i][j] = 0

print(ans)



# 참고
from collections import deque
from sys import stdin

input1 = stdin.readline
directions = (
    (0, 1),  # 우
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
)


def is_in_range(obj, a, b):
    if isinstance(obj, int):
        return 0 <= a < obj and 0 <= b < obj
    else:
        return 0 <= a < len(obj) and 0 <= b < len(obj)


class Context:
    def __init__(self, arr, visit, r, c):
        self.arr, self.visit, self.r, self.c = arr, visit, r, c
        self.population = arr[r][c]
        self.positions = [(r, c)]
        self.visit[r][c] = True

    def __repr__(self):
        return str(self.positions)

    def visit_func(self, x, y):
        self.visit[x][y] = True
        self.population += self.arr[x][y]
        self.positions.append((x, y))


def bfs(arr, visit, _r, _c, l1, r1) -> Context:
    context = Context(arr, visit, _r, _c)
    q = deque([[(_r, _c)]])
    while q:
        popped = q.popleft()
        next_pos = []
        for r, c in popped:
            for a, b in directions:
                x, y = a + r, b + c
                if not is_in_range(len(arr), x, y) or visit[x][y]:
                    continue
                if l1 <= abs(arr[x][y] - arr[r][c]) <= r1:
                    next_pos.append((x, y))
                    context.visit_func(x, y)
        if next_pos:
            q.append(next_pos)
    return context


def move(context: Context, new_candidates):
    new_population = context.population // len(context.positions)
    for r, c in context.positions:
        context.arr[r][c] = new_population
        new_candidates.add((r, c))


def solution():
    n, l, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = -1
    candidates = deque([(i, j) for i in range(n) for j in range(i % 2, n, 2)])
    while True:
        visit = [[False] * len(arr) for _ in range(len(arr))]
        contexts = []
        for i, j in candidates:
            contexts.append(bfs(arr, visit, i, j, l, r))
        if not contexts:
            break
        new_candidates = set([])
        for context in contexts:
            if len(context.positions) > 1:
                move(context, new_candidates)
        candidates = new_candidates
        cnt += 1
    print(cnt)


if __name__ == "__main__":
    solution()
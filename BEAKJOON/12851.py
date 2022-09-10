# 12851. 숨바꼭질 2  2022-09-10


from collections import deque


N, K = map(int, input().split())
v = [[0, 0] for _ in range(100001)]

v[N][1] = 1
q = deque()
q.append(N)

while q:
    n = q.popleft()
    if v[K][1] and v[n][0] > v[K][0]:
        break

    for next in [n - 1, n + 1, n * 2]:
        if 0 <= next <= 100000:
            if not v[next][0]:
                v[next][0] = v[n][0] + 1
                v[next][1] += v[n][1]
                q.append(next)
            elif v[next][0] == v[n][0] + 1:
                v[next][1] += v[n][1]

print(v[K][0])
print(v[K][1])
# 미로 탈출 명령어 2023 KAKAO BLIND RECRUITMENT  2023-04-12


from collections import deque


def solution(N, M, si, sj, ei, ej, K):
    gap = K - abs(si - ei) - abs(sj - ej)
    if gap < 0 or gap % 2 == 1:
        return "impossible"

    q = deque()
    q.append((si, sj, []))
    while q:
        i, j, path = q.popleft()

        if len(path) > K: continue
        if i == ei and j == ej and len(path) == K:
            return "".join(path)

        for di, dj, d in [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]:
            ni, nj = i + di, j + dj
            if not (1 <= ni <= N) or not (1 <= nj <= M): continue
            if abs(ni - ei) + abs(nj - ej) + len(path) + 1 > K: continue

            q.append((ni, nj, path + [d]))
            break
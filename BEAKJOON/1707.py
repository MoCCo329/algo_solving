# 1707. 이분 그래프  2023-02-22


from collections import deque


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_matrix = [[]for _ in range(V + 1)]
    color = [-1] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        adj_matrix[a].append(b)
        adj_matrix[b].append(a)

    ans = True
    q = deque()

    for n in range(1, V + 1):
        if color[n] != -1: continue
        q.append((n, 1))

        while q:
            v, cnt = q.popleft()
            color[v] = cnt % 2

            for i in adj_matrix[v]:
                if color[i] == color[v]:
                    ans = False
                    break
                if color[i] != -1: continue
                q.append((i, cnt + 1))

            if not ans: break
        if not ans: break

    print("YES" if ans else "NO")
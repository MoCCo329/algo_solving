# 5248. 그룹 나누기 2022-04-04

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    adjL = [[i] for i in range(N + 1)]
    for i in range(M):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        adjL[n1].append(n2)
        adjL[n2].append(n1)

    v = [0] * (N + 1)
    for i in range(1, N + 1):
        if v[i] == 0:
            v[0] += 1  # v[0]은 cnt
            q = [i]
            while q:
                j = q.pop(0)
                v[j] = 1
                for k in adjL[j]:
                    if v[k] == 0:
                        q.append(k)
    print(f'#{tc} {v[0]}')


# def find_set(x):
#     while x != p[x]:
#         x = p[x]
#     return x
#
#
# def union_set(x, y):
#     p[find_set(y)] = find_set(x)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     p = [i for i in range(N + 1)]
#     for i in range(M):
#         n1, n2 = arr[i * 2], arr[i * 2 + 1]
#         union_set(n1, n2)
#     ans = [find_set(i) for i in range(1, N + 1)]
#     print(f'#{tc} {len(set(ans))}')
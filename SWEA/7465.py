# 7465. 창용 마을 무리의 개수 2022-04-04

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adjL = [[0]] * (N + 1)
    v = [0] * (N + 1)
    for _ in range(M):
        n1, n2 = map(int, input().split())
        if adjL[n1][0]:
            adjL[n1].append(n2)
        else:
            adjL[n1] = [n2]
        if adjL[n2][0]:
            adjL[n2].append(n1)
        else:
            adjL[n2] = [n1]

    cnt = 0
    for i in range(1, N + 1):
        if v[i] == 0:
            cnt += 1
            q = []
            q.append(i)
            v[i] = 1
            while q:
                j = q.pop(0)
                for k in adjL[j]:
                    if v[k] == 0:
                        q.append(k)
                        v[k] = 1

    print(f'#{tc} {cnt}')
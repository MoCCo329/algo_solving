T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0
    q = [(N, 0)]
    front = 0
    v = [0] * 1000001
    v[N] = 1
    while q:
        i, cnt = q[front]
        front += 1
        for j in [i + 1, i - 1, i * 2, i - 10]:
            if 0 < j <= 1000000 and not v[j]:
                v[j] = 1
                if j == M:
                    ans = cnt + 1
                    break
                else:
                    q.append((j, cnt + 1))
        if ans:
                break
    print(f'#{tc} {ans}')
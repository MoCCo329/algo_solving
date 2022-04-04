T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    schedule.sort(key = lambda x: (x[1] - x[0], x[0]))
    v = [0] * 24
    cnt = 0

    for i in range(N):
        if not 1 in v[schedule[i][0]:schedule[i][1]]:
            for j in range(schedule[i][0], schedule[i][1]):
                v[j] = 1
            cnt += 1

    print(f'#{tc} {cnt}')
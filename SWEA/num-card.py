for T in range(int(input())):
    N = int(input())
    num = input()
    counts = [0] * 10
    for i in range(N):
        counts[int(num[i])] += 1

    cnt_max = 0
    idx_max = 0

    for idx, cnt in enumerate(counts):
        if cnt >= cnt_max:
            cnt_max = cnt
            idx_max = idx


    print(f'#{T+1} {idx_max} {cnt_max}')
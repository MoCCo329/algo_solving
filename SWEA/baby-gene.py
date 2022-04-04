T = int(input())
for tc in range(1, T+1):
    num = input()

    c = [0] * 12
    for i in range(6):
        c[int(num[i])] += 1

    tri = 0
    ru = 0
    i = 0
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] > 0 and c[i+1] > 0 and c[i+2] > 0:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            ru += 1
            continue
        i += 1

    if ru + tri == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
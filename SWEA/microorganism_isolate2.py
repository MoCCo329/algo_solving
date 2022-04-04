def turn():  # K 는 g_list의 길이
    global g_list
    L = len(g_list)

    # 모든 군집을 이동시키기
    for idx in range(L):
        i, j, c, d_idx = g_list[idx]
        di, dj = d_list[d_idx]
        i, j = i + di, j + dj

        if 0 < i < N-1 and 0 < j < N-1:  # 경계가 아닌 경우 이동만 한다.
            g_list[idx][0] = i
            g_list[idx][1] = j

        else:  # 경계인 경우 이동하고, 절반으로 줄어들고, 방향이 바뀐다.
            if d_idx % 2 == 0:
                d_idx -= 1
            else:
                d_idx += 1
            g_list[idx] = [i, j, c//2, d_idx]

    # 만나는게 있는경우
    cnt = 0
    i = 0
    while i < L-1 - cnt:
        sumK = g_list[i][2]
        j = i+1
        while j < L - cnt:
            if g_list[i][0] == g_list[j][0] and g_list[i][1] == g_list[j][1]:
                sumK += g_list[j][2]
                if g_list[i][2] < g_list[j][2]:
                    g_list[i][3] = g_list[j][3]
                    g_list[i][2] = g_list[j][2]
                g_list.pop(j)  # 뒤에것은 없앤다
                cnt += 1
            else:
                j += 1
        g_list[i][2] = sumK  # 앞에것의 미생물 수를 sumK로
        i += 1

d_list = [0, [-1, 0], [1, 0], [0, -1], [0, 1]]  # 1상 2하 3좌 4우
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    g_list = []
    for _ in range(K):
        g_list += [list(map(int, input().split()))]

    for _ in range(M):
        turn()

    cnt = 0
    for group in g_list:
        cnt += group[2]

    print(f'#{tc} {cnt}')
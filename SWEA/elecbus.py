for T in range(int(input())):
    k, n, m = map(int, input().split())
    m_list = list(map(int, input().split())) + [n]

    charge_cnt = 0
    battery_now = k
    m_idx = 0
    for i in range(1, n):
        if m_list[m_idx] == i and battery_now-1 < m_list[m_idx+1]-i:
            m_idx += 1
            charge_cnt += 1
            battery_now = k
        elif m_list[m_idx] == i and battery_now-1 >= m_list[m_idx+1]-i:
            m_idx += 1
            battery_now -= 1
        else:
            battery_now -= 1

        if battery_now == 0:
            charge_cnt = 0
            break

    print(f'#{T+1} {charge_cnt}')
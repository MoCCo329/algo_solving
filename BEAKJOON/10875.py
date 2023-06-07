# 10875. 뱀  2023-06-07


L = int(input())
N = int(input())
x, y = 0, 0
lines = []
d_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d = 0
t = 0

for k in range(N + 1):
    if k == N:
        l, dd = 3 * L, 0
    else:
        l, dd = input().split()
    l = int(l)
    dx, dy = d_list[d]
    nx, ny = x + dx * l, y + dy * l
    type = d % 2  # 0 이면 가로줄, 1이면 세로줄
    new_line = (min(x, nx), min(y, ny), max(x, nx), max(y, ny), type)

    dt = 3 * L
    if type == 0 and (new_line[0] < -L or new_line[2] > L):
        dt = L + 1 - x if d == 0 else x + L + 1
    elif type == 1 and (new_line[1] < -L or new_line[3] > L):
        dt = L + 1 - y if d == 1 else y + L + 1
    for line in lines[:-1]:
        if type == 1:
            if line[4] == 1:
                if line[0] != new_line[0]: continue
                if line[3] < new_line[1] or line[1] > new_line[3]: continue
                dt = min(dt, abs(y - line[1]), abs(y - line[3]))
            else:
                if not (new_line[1] <= line[1] <= new_line[3]): continue
                if not (line[0] <= new_line[0] <= line[2]): continue
                dt = min(dt, abs(y - line[1]))
        else:
            if line[4] == 1:
                if not (line[1] <= new_line[1] <= line[3]): continue
                if not (new_line[0] <= line[0] <= new_line[2]): continue
                dt = min(dt, abs(x - line[0]))
            else:
                if line[1] != new_line[1]: continue
                if line[2] < new_line[0] or line[0] > new_line[2]: continue
                dt = min(dt, abs(x - line[0]), abs(x - line[2]))
    if dt != 3 * L:
        print(t + dt)
        exit(0)
    lines.append(new_line)
    
    x += dx * l
    y += dy * l
    t += l
    d = (d + (1 if dd == 'L' else -1)) % 4
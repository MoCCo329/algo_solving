# 2623. 음악프로그램  2022-08-02


N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    num, *V_list = map(int, input().split())
    before = 0
    for V in V_list:
        if before:
            arr[before][V] = 1
        before = V

v = [0] * (N + 1)
ind = [0] * (N + 1)
for j in range(1, N + 1):
    for i in range(1, N + 1):
        if arr[i][j]:
            ind[j] += 1

path = []
while True:
    for i in range(1, N + 1):
        if ind[i] == 0 and v[i] == 0:
            path.append(i)
            for j in range(1, N + 1):
                if arr[i][j]:
                    ind[j] -= 1
            v[i] = 1
            break
    else:
        if len(path) != N:
            print(0)
            break
        else:
            print(*path, sep='\n')
            break
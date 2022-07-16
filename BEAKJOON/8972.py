# 8972. 미친 아두이노  2022-07-16


d_list = [0, [1, -1], [1, 0], [1, 1], [0, -1], [0, 0], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
moves = list(map(int, input()))

R_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == "I":
            I, J = i, j
            arr[i][j] = "."
        elif arr[i][j] == "R":
            R_list.append((i, j))
            arr[i][j] = "."

for step in range(len(moves)):
    # 종수 이동
    di, dj = d_list[moves[step]]
    I, J = I + di, J + dj
    if (I, J) in R_list:
        print(f'kraj {step + 1}')
        exit(0)

    # 미친 아두이노 이동
    new_R = set()
    pop_R = set()
    for R in R_list:
        ri, rj = R
        min_dist = abs(I - ri) + abs(J - rj)
        min_idx = 5
        for d in range(1, 10):
            if min_dist > abs(I - ri - d_list[d][0]) + abs(J - rj - d_list[d][1]):
                min_dist = abs(I - ri - d_list[d][0]) + abs(J - rj - d_list[d][1])
                min_idx = d

        ni, nj = ri + d_list[min_idx][0], rj + d_list[min_idx][1]
        if (I, J) == (ni, nj):
            print(f'kraj {step + 1}')
            exit(0)
        if (ni, nj) in new_R:
            pop_R.add((ni, nj))
        else:
            new_R.add((ni, nj))

    for R in pop_R:
        new_R.remove(R)
    R_list = new_R

arr[I][J] = "I"
for R in R_list:
    ri, rj = R
    arr[ri][rj] = "R"
for i in range(N):
    print("".join(arr[i]))
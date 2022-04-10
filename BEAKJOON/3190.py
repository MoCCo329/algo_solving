# 3190. 뱀 2022-04-10

d_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
arr[0][0] = 1
for _ in range(K):
    i, j = map(int, input().split())
    arr[i - 1][j - 1] = 2
L = int(input())
moves = []
for _ in range(L):
    sec, direc = input().split()
    moves.append([int(sec), direc])
moves.append([10001, "D"])


q = [(0, 0)]
s_now = 0
d_now = 0
for sec, direc in moves:
    di, dj = d_list[d_now]

    for s_prog in range(1, sec - s_now + 1):
        hi, hj = q[-1]
        ni, nj = hi + di, hj + dj
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                q.append((ni, nj))
                arr[hi][hj] = 1
                ti, tj = q.pop(0)
                arr[ti][tj] = 0
            elif arr[ni][nj] == 2:
                q.append((ni, nj))
                arr[hi][hj] = 1
            else:
                print(s_now + s_prog)
                exit(0)
        else:
            print(s_now + s_prog)
            exit(0)

    if direc == "L":
        d_now = (d_now - 1) % 4
    else:
        d_now = (d_now + 1) % 4
    s_now = sec

print(10000)
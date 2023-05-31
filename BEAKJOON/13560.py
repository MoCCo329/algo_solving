# 13560. 축구 게임  2023-05-31


N = int(input())
arr = sorted(list(map(int, input().split())))

tot = arr[0]
s = 0
for i in range(1, N):
    tot += arr[i]
    s += i
    if s > tot:
        print(-1)
        break
else:
    if tot == N * (N - 1) // 2:
        print(1)
    else:
        print(-1)
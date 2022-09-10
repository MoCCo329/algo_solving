# 2096. 내려가기  2022-09-10


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

before = arr[0]
for i in range(1, N):
    next = [0] * 3
    next[0] = max(before[0], before[1]) + arr[i][0]
    next[1] = max(before[0], before[1], before[2]) + arr[i][1]
    next[2] = max(before[1], before[2]) + arr[i][2]
    before = next
max_v = max(before)

before = arr[0]
for i in range(1, N):
    next = [0] * 3
    next[0] = min(before[0], before[1]) + arr[i][0]
    next[1] = min(before[0], before[1], before[2]) + arr[i][1]
    next[2] = min(before[1], before[2]) + arr[i][2]
    before = next
print(max_v, min(before))
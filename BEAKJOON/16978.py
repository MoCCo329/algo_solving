# 16978. 수열과 쿼리 22  2023-06-22


import sys
input = sys.stdin.readline


def update(i, v):
    i += 1
    while i < N + 1:
        fwt[i] += v
        i += i & -i


def get(i):
    temp = 0
    i += 1
    while 0 < i:
        temp += fwt[i]
        i &= i - 1
    return temp


N = int(input())
arr = list(map(int, input().split()))
fwt = [0] * (N + 1)
for i in range(N):
    update(i, arr[i])
get_querys = []
update_querys = []
cnt = 0
for _ in range(int(input())):
    order, *nums = map(int, input().split())
    if order == 1:
        update_querys.append((nums[0] - 1, nums[1]))
    else:
        get_querys.append((nums[0], nums[1] - 1, nums[2] - 1, cnt))
        cnt += 1
get_querys.sort()

ans = [0] * cnt
ui = 0
gi = 0
while gi < cnt:
    while ui < get_querys[gi][0]:
        i, v = update_querys[ui]
        gap = v - arr[i]
        arr[i] = v
        update(i, gap)
        ui += 1
    temp1 = get(get_querys[gi][2])
    temp2 = 0 if get_querys[gi][1] == 0 else get(get_querys[gi][1] - 1)
    ans[get_querys[gi][3]] = temp1 - temp2
    gi += 1

for i in range(cnt):
    print(ans[i])
# 14897. 서로 다른 수와 쿼리 1  2023-06-23


import sys
input = sys.stdin.readline


N = int(input())
temp_arr = list(map(int, input().split()))
arr = []
nums = {}
idx = 0
for n in temp_arr:
    if n not in nums:
        nums[n] = idx
        arr.append(idx)
        idx += 1
    else:
        arr.append(nums[n])

M = int(input())
querys = [(*map(lambda x: int(x) - 1, input().split()), i) for i in range(M)]
k = int(M ** 0.5)
querys.sort(key=lambda x: (x[1] // k, x[0]))

ans = [0] * M
counts = [0] * idx

cnt = 0
tot = 0
for i in range(querys[0][0], querys[0][1] + 1):
    counts[arr[i]] += 1
    if counts[arr[i]] == 1:
        cnt += 1
ans[querys[0][2]] = cnt

i, j = querys[0][0], querys[0][1]
for k in range(1, M):
    if i < querys[k][0]:
        while i < querys[k][0]:
            counts[arr[i]] -= 1
            if counts[arr[i]] == 0:
                cnt -= 1
            i += 1
    elif querys[k][0] < i:
        while querys[k][0] < i:
            i -= 1
            counts[arr[i]] += 1
            if counts[arr[i]] == 1:
                cnt += 1
    if j < querys[k][1]:
        while j < querys[k][1]:
            j += 1
            counts[arr[j]] += 1
            if counts[arr[j]] == 1:
                cnt += 1
    elif querys[k][1] < j:
        while querys[k][1] < j:
            counts[arr[j]] -= 1
            if counts[arr[j]] == 0:
                cnt -= 1
            j -= 1
    ans[querys[k][2]] = cnt

print(*ans, sep="\n")
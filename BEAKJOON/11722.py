# 11722. 가장 긴 감소하는 부분 수열  2023-01-17


def lower_bound(n):
    s, e = 0, len(ans) - 1
    min_idx = len(ans)

    while s <= e:
        m = (s + e) // 2

        if n >= ans[m]:
            e = m - 1
            min_idx = min(min_idx, m)
        else:
            s = m + 1

    return min_idx


N = int(input())
arr = list(map(int, input().split()))

ans = [arr[0]]
for i in range(1, N):
    if ans[-1] > arr[i]:
        ans.append(arr[i])
    elif ans[-1] < arr[i]:
        ans[lower_bound(arr[i])] = arr[i]

print(len(ans))
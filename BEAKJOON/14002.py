# 14002. 가장 긴 증가하는 부분 수열 4  2023-01-15


def lower_bound(n):
    s, e = 0, len(ans) - 1

    while s <= e:
        m = (s + e) // 2

        if n <= ans[m]:
            e = m - 1
        else:
            s = m + 1

    return s


N = int(input())
arr = list(map(int, input().split()))

ans = [arr[0]]
dp = [1] + [0] * (N - 1)
for i in range(1, N):
    if ans[-1] < arr[i]:
        ans.append(arr[i])
        dp[i] = len(ans)
    elif ans[-1] > arr[i]:
        idx = lower_bound(arr[i])
        ans[idx] = arr[i]
        dp[i] = idx + 1

path = []
l = len(ans)
for i in range(N - 1, -1, -1):
    if l == dp[i]:
        path.append(arr[i])
        l -= 1

    if l == 0: break

print(len(ans))
print(*path[::-1])
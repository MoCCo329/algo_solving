# 1806. 부분합  2022-08-03


N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = N + 1
i = 0
j = 0
temp = arr[0]
while i <= j:
    if temp >= S:
        ans = min(ans, j - i + 1)
        if i != N - 1:
            temp -= arr[i]
            i += 1
        else:
            break
    else:
        if j != N - 1:
            j += 1
            temp += arr[j]
        else:
            break
if ans == N + 1:
    ans = 0

print(ans)
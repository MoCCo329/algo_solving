# 3273 S3 2022-06-30

N = int(input())
arr = list(map(int, input().split()))
X = int(input())
ans = 0

arr.sort()
j = N - 1
for i in range(N):
    while arr[i] + arr[j] > X:
        j -= 1

    if i >= j:
        break

    if arr[i] + arr[j] == X:
        ans += 1

print(ans)
# 2467. 용액  2022-08-02


N = int(input())
arr = list(map(int, input().split()))

i = 0
j = N - 1

min_gap = abs(arr[i] + arr[j])
ans = [0, N - 1]
while i < j:
    temp = arr[i] + arr[j]
    if abs(temp) < min_gap:
        min_gap = abs(temp)
        ans = [i, j]
    if temp == 0:
        ans = [i, j]
        break
    elif temp < 0:
        i += 1
    else:
        j -= 1
print(arr[ans[0]], arr[ans[1]])
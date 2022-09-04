# 2473. 세 용액  2022-09-04


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = []
ans_tot = 3000000000
for i in range(N - 2):
    j = i + 1
    k = N - 1
    while j < k:
        tot = arr[i] + arr[j] + arr[k]
        if abs(ans_tot) > abs(tot):
            ans = [i, j, k]
            ans_tot = tot

        if tot == 0:
            break
        elif tot > 0:
            k -= 1
        else:
            j += 1

for i in range(3):
    print(arr[ans[i]], end=' ')
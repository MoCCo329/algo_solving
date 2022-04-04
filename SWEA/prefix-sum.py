# for T in range(int(input())):
#     n, m = tuple(map(int, input().split()))
#     arr = list(map(int, input().split()))
#     maxV = 0
#     minV = 0
#     for i in range(m):
#         minV += arr[i]
#         maxV += arr[i]
#
#     for i in range(n - m + 1):
#         sum = 0
#         for j in range(m):
#             sum += arr[i + j]
#         if maxV < sum:
#             maxV = sum
#         if minV > sum:
#             minV = sum
#     print(f'#{T + 1} {maxV - minV}')

for T in range(int(input())):
    n, m = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    sum_temp = 0
    sum_max = 0
    sum_min = 0
    for i in range(m):
        sum_temp += arr[i]
        sum_max += arr[i]
        sum_min += arr[i]

    for i in range(n-m):
        sum_temp -= arr[i]
        sum_temp += arr[i+m]

        if sum_temp > sum_max:
            sum_max = sum_temp
        if sum_temp < sum_min:
            sum_min = sum_temp

    print(f'#{T+1} {sum_max - sum_min}')
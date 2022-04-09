# 13458. 시험 감독 2022-04-09

N = int(input())
A_arr = list(map(int, input().split()))
B, C = map(int, input().split())

for i in range(N):
    temp = A_arr[i] - B
    if temp > 0:
        A_arr[i] = 1 + temp // C + bool(temp % C)
    else:
        A_arr[i] = 1

print(sum(A_arr))
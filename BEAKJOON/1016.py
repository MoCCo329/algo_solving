# 1016. 제곱 ㄴㄴ 수  2023-03-22


import math


s, e = map(int, input().split())
end = int(math.sqrt(e)) + 1
vis = [1] * end
ans_arr = [1] * (e - s + 1)

for i in range(2, end):
    if vis[i] == 0: continue

    n = i * i
    temp = i
    while temp < end:
        vis[temp] = 0
        temp += i

    temp = (s // n) * n
    while temp <= e:
        if s <= temp:
            ans_arr[temp - s] = 0
        temp += n

print(sum(ans_arr))
# 1654. 랜선 자르기  2023-01-16


def test(m):  # m 길이로 잘라낸 개수를 반환
    tot = 0
    for l in L_list:
        tot += l // m
    return tot


K, N = map(int, input().split())
L_list = [int(input()) for _ in range(K)]

left = 1
right = max(L_list)

ans = 1
while left <= right:
    mid = (left + right) // 2

    result = test(mid)
    if result >= N:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)
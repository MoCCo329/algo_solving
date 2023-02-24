# 1517. 버블 소트  2023-02-24


N = int(input())
nums = list(map(int, input().split()))
hashMap = dict()
for i, n in enumerate(sorted(nums)):
    hashMap[n] = i

k = 1
while k < N: k <<= 1
st = [0] * (k << 1)

ans = 0
for n in nums:
    i = hashMap[n]
    start = k + i
    end = k + N - 1

    temp = 0
    while start <= end:
        if start % 2 == 1:
            temp += st[start]
        if end % 2 == 0:
            temp += st[end]
        start = (start + 1) // 2
        end = (end - 1) // 2

    if st[k + i] == 1: temp -= 1
    st[k + i] = 1
    i = (k + i) // 2
    while i > 0:
        st[i] = st[i * 2] + st[i * 2 + 1]
        i >>= 1

    ans += temp

print(ans)
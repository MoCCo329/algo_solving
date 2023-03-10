# 1786. 찾기  2023-03-10


T = input()
P = input()
tL = len(T)
pL = len(P)
lps = [0] * pL

j = 0
for i in range(1, pL):
    while j > 0 and P[i] != P[j]:
        j = lps[j - 1]

    if P[i] == P[j]:
        j += 1
        lps[i] = j

ans = 0
ans_list = []

j = 0
for i in range(tL):
    while j > 0 and T[i] != P[j]:
        j = lps[j - 1]

    if T[i] == P[j]:
        if j == pL - 1:
            ans += 1
            ans_list.append(i - pL + 2)
            j = lps[j]
        else:
            j += 1

print(ans)
print(*ans_list)
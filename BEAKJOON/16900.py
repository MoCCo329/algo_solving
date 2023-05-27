# 16900. 이름 정하기  2023-05-27


S, K = input().split()
L = len(S)
K = int(K)

pf = [0] * L
j = 0
for i in range(1, L):
    while j != 0 and S[j] != S[i]:
        j = pf[j - 1]

    if S[j] == S[i]:
        j += 1
    pf[i] = j

print((L - pf[-1]) * (K - 1) + L)
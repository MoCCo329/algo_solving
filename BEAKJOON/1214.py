# 1214. 쿨한 물건 구매  2023-05-19


D, P, Q = map(int, input().split())

P, Q = (P, Q) if Q < P else (Q, P)  # P > Q

if D % P == 0 or D % Q == 0:
    print(D)
else:
    ans = (D + P - 1) // P * P
    for i in range(Q + 1):
        if D < i * P: continue
        ans = min(ans, i * P + (D - i * P + Q - 1) // Q * Q)
    print(ans)
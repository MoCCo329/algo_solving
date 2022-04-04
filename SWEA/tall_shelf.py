# def f(i, c, N, M):  # N개 중에서 M개를 선택하는 조합. c는 현재 저장된 답안 개수, i는 진행된 인덱스
#     global ans, chk, B
#     if c == M:
#         tot = sum(ans_temp)
#         if B <= tot < ans:
#             ans = tot
#     elif M-c > N-i:
#         return
#     else:
#         for j in range(i, N):
#             if v[j] == True:
#                 continue
#             else:
#                 ans_temp[c] = t_list[j]
#                 v[j] = True
#                 f(j+1, c+1, N, M)
#                 v[j] = False
#
# T = int(input())
# for tc in range(1, T+1):
#     N, B = map(int, input().split())
#     t_list = sorted(list(map(int, input().split())))
#     ans = 2*B
#     ans_temp = [0] * N
#     v = [0] * (N + 1)
#
#     M = 2
#     while M <= N:
#         f(0, 0, N, M)
#         M += 1
#
#     print(f'#{tc} {ans-B}')

def boo(i, n, s, rs):
    global res
    if s >= B:
        if s < res:
            res = s
    elif i == n:
        return
    elif s + rs < B:
        return
    else:
        boo(i + 1, n, s + staff[i], rs - staff[i])
        boo(i + 1, n, s, rs)

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    staff = list(map(int, input().split()))
    res = sum(staff)
    boo(0, N, 0, res)
    print(f'#{tc} {res - B}')
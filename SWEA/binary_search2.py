def in_order(n, N):
    global cnt
    if n <= N:
        in_order(2*n, N)
        tree[n] = cnt
        cnt += 1
        in_order(2*n+1, N)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 1
    tree = [0] * (N + 1)
    in_order(1, N)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
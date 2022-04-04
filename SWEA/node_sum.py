def post_order(n, N):
    global chk
    if n > N:
        chk += 1
    else:
        post_order(n*2, N)
        post_order(n*2+1, N)
        if chk == 2:
            chk = 0
        elif chk == 1:
            tree[n] = tree[n*2]
            chk = 0
        else:
            tree[n] = tree[n*2] + tree[n*2+1]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int,input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v

    chk = 0
    post_order(1, N)
    print(f'#{tc} {tree[L]}')
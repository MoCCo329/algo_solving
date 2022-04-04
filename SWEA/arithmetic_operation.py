def post_order(v):
    if v:
        if type(tree[v]) == str:
            r = post_order(c1[v])
            l = post_order(c2[v])
            if tree[v]== '+':
                return r+l
            elif tree[v] == '-':
                return r-l
            elif tree[v] == '*':
                return r*l
            else:
                return r/l
        else:
            return tree[v]

for tc in range(1, 11):
    N = int(input())
    tree = [[0, 0] for _ in range(N + 1)]
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    for _ in range(N):
        n, v, *c = map(str, input().split())
        if len(c) == 0:
            tree[int(n)] = int(v)
        else:
            tree[int(n)] = v
            c1[int(n)] = int(c[0])
            c2[int(n)] = int(c[1])

    print(f'#{tc} {int(post_order(1))}')
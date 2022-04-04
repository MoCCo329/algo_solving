def in_order(v):
    global ans
    if v:
        in_order(ch1[v])
        ans += [arr[v]]
        in_order(ch2[v])

for tc in range(1, 11):
    V = int(input()) # 노드 수
    arr = [0] # 인덱스에 해당 노드번호 알파벳이 담긴다.
    for i in range(V):
        node, *alpha = input().split()
        arr.append(alpha[0])

    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    for i in range(1, (V+1)//2):
        ch1[i] = 2*i
        ch2[i] = 2*i + 1
    if V%2 == 0:
        ch1[V//2] = V

    ans = []
    in_order(1)
    print(f'#{tc}', end=' ')
    for alpha in ans:
        print(alpha, end='')
    print()
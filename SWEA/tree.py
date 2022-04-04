T = int(input())
for tc in range(1, T+1):
    # 입력 받기
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    ch1 = [0]*(E+2) # 부모를 인덱스로 자식번호 저장
    ch2 = [0]*(E+2)
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    # def pre_order(v):
    #     if v:  # 존재하는 정점이면
    #         print(v, end=' ')  # visit()
    #         pre_order(ch1[v])  # 왼쪽 자식 노드로 이동
    #         pre_order(ch2[v])  # 오른쪽 자식 노드로 이동
    #
    # def in_order(v):
    #     if v:
    #         in_order(ch1[v])
    #         print(V, end=' ')
    #         in_order(ch2[v])

    def post_order(v):
        global cnt, ans

        if v:
            post_order(ch1[v])
            post_order(ch2[v])

            cnt += 1
            if v == N:
                return cnt

    cnt = 0
    ans = 0
    print(f'#{tc} {post_order(N)}')
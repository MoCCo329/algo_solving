def bfs(v):
    global maxV, ans_list
    q = [v]
    visited[v] = 1

    while q:
        nv = q.pop(0)
        if maxV < visited[nv]:  # 더 늦게 연락된 곳이면 저장
            ans_list = [nv]
            maxV = visited[nv]
        elif maxV == visited[nv]:
            ans_list += [nv]

        for nnv in c[nv]:
            if visited[nnv] == 0:
                visited[nnv] = visited[nv] + 1
                q += [nnv]

for tc in range(1, 11):
    N, root = map(int, input().split())
    arr = list(map(int, input().split()))
    c = [[] for _ in range(N + 1)]  # 자손 리스트
    for i in range(N//2):
        c[arr[2*i]] += [arr[2*i + 1]]

    visited = [0] * (101)  # 연락된 곳인지 기록
    ans_list = []
    maxV = 0

    bfs(root)
    print(f'#{tc} {max(ans_list)}')
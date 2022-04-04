def dfs(cnt, N, W, H):  # cnt 구슬 번호 (0부터 시작)
    global ans
    if cnt == N:
        temp_ans = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j]:
                    temp_ans += 1
        if temp_ans < ans:
            ans = temp_ans

    for i in range(W):
        # 삭제하기
        pop_set = set()
        for j in range(H - 1, -1, -1):
            if arr[j][i]:
                pop_num = arr[j][i]
                pop_set([i, j])
                for k in range(1, pop_num):
                    pop_set.add([i, j - k])
                    pop_set.add([i, j + k])

                    for ii in range(i - pop_num + 1, i + pop_num):
                        jj = 0
                        for _ in range(j - 1):
                            jj = arr[ii][jj]
                            if arr[ii][jj] <= H:



                    pop_set.add([i - k, j])

                v[i][j - pop_num] = j + pop_num


        # 재귀

        # 복귀


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    v = [[i + 1 for i in range(H)] for _ in range(W)]  # 가로세로 전치됨 주의

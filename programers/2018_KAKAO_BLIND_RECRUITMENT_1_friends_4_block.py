# [1차] 프렌즈4블록 2018 KAKAO BLIND RECRUITMENT  2022-06-01


def solution(m, n, board):
    new_arr = [[board[j][i] for j in range(m)] for i in range(n)]

    # for i in range(n):
    #     print(new_arr[i])

    d_list = [[[-1, -1], [-1, 0], [0, -1]], [[-1, 0], [-1, 1], [0, 1]], [[0, -1], [1, -1], [1, 0]],
              [[0, 1], [1, 0], [1, 1]]]
    ans = 0
    chk = 1

    while chk == 1:
        # 사라질 박스 체크
        chk = 0
        v = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if new_arr[i][j] != 0:
                    for k in range(4):
                        for di, dj in d_list[k]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < m and new_arr[i][j] == new_arr[ni][nj]:
                                pass
                            else:
                                break
                        else:
                            chk = 1
                            for di, dj in d_list[k]:
                                v[i + di][j + dj] = 1

        # 박스 지우기
        for i in range(n):
            for j in range(m):
                if v[i][j] == 1:
                    ans += 1
                    new_arr[i][j] = 0

        # 지운 박스 내리기
        for i in range(n):
            temp_arr = []
            for j in range(m):
                if new_arr[i][j] != 0:
                    temp_arr.append(new_arr[i][j])
            temp_arr = [0] * (m - len(temp_arr)) + temp_arr
            new_arr[i] = temp_arr

    return ans

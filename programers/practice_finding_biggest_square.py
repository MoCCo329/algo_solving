def solution(board):
    N = len(board)
    M = len(board[0])

    arr = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            arr[i][j] = board[i - 1][j - 1] + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

    ans = 0
    for k in range(1, min(N, M) + 1):
        chk = 0
        temp = k ** 2
        for i in range(N - k + 1):
            for j in range(M - k + 1):
                if arr[i + k][j + k] - arr[i + k][j] - arr[i][j + k] + arr[i][j] == temp:
                    chk = 1
                    ans = temp
                    break
            if chk:
                break

    return ans


def solution(board):
    N = len(board)
    M = len(board[0])

    arr = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            arr[i][j] = board[i - 1][j - 1] + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

    ans = 0

    # parametric search로 한변Mid 구하기
    L = 0
    R = min(N, M)
    while L <= R:
        Mid = (L + R) // 2

        chk = 0
        temp = Mid ** 2
        for i in range(N - Mid + 1):
            for j in range(M - Mid + 1):
                if arr[i + Mid][j + Mid] - arr[i + Mid][j] - arr[i][j + Mid] + arr[i][j] == temp:
                    chk = 1
                    ans = max(ans, temp)
                    break
            if chk:
                break
        if chk:
            L = Mid + 1
        else:
            R = Mid - 1

    return ans
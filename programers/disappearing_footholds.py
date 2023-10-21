# 사라지는 발판.  2023-10-21


def dfs(cnt, i1, j1, i2, j2):
    global board
    
    if cnt % 2 == 0:
        board[i1][j1] = 0
    else:
        board[i2][j2] = 0
    
    w_cnt = []
    l_cnt = []
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = (i1 + di, j1 + dj) if cnt % 2 == 0 else (i2 + di, j2 + dj)
        if ni < 0 or len(board) <= ni or nj < 0 or len(board[0]) <= nj or board[ni][nj] == 0: continue
        temp = dfs(cnt + 1, ni, nj, i2, j2) if cnt % 2 == 0 else dfs(cnt + 1, i1, j1, ni, nj)
        if cnt % 2 == 0:
            if temp[0] == 1:
                w_cnt.append(temp[1])
            else:
                l_cnt.append(temp[1])
        else:
            if temp[0] == 1:
                l_cnt.append(temp[1])
            else:
                w_cnt.append(temp[1])
    
    if cnt % 2 == 0:
        board[i1][j1] = 1
    else:
        board[i2][j2] = 1
    
    if len(w_cnt) == 0 and len(l_cnt) == 0:
        return [0 if cnt % 2 == 0 else 1, cnt]
    if (i1, j1) == (i2, j2):
        return [1 if cnt % 2 == 0 else 0, cnt + 1]
    if len(w_cnt):
        return [cnt % 2 == 0, min(w_cnt)]
    else:
        return [cnt % 2 != 0, max(l_cnt)]


def solution(_board, aloc, bloc):
    global board
    
    board = _board
    return dfs(0, aloc[0], aloc[1], bloc[0], bloc[1])[1]

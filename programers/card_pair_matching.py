# 카드 짝 맞추기.  2023-12-25


def move(i1, j1, i2, j2):
    global m_vis
    
    vis = [[False] * 4 for _ in range(4)]
    q = [(i1, j1, 0)]
    vis[i1][j1] = True
    while q:
        i, j, d = q.pop(0)
        if i == i2 and j == j2: return d
    
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 4 and 0 <= nj < 4 and not vis[ni][nj]:
                vis[ni][nj] = True
                q.append((ni, nj, d + 1))
            
            while 0 <= ni < 4 and 0 <= nj < 4 and board[ni][nj] == 0:
                ni += di
                nj += dj
            if not (0 <= ni < 4) or not (0 <= nj < 4):
                ni -= di
                nj -= dj
            if vis[ni][nj]: continue
            vis[ni][nj] = True
            q.append((ni, nj, d + 1))

    return 6


def dfs(cnt, i, j, k):
    global ans, goal
    
    if k == goal:
        ans = min(ans, cnt)
        return
    
    for l in range(1, goal + 1):
        if vis[l]: continue
        vis[l] = True
        d1 = move(i, j, *pos[l][0])
        board[pos[l][0][0]][pos[l][0][1]] = 0
        d2 = move(*pos[l][0], *pos[l][1])
        board[pos[l][1][0]][pos[l][1][1]] = 0
        dfs(cnt + d1 + d2, pos[l][1][0], pos[l][1][1], k + 1)
        board[pos[l][0][0]][pos[l][0][1]] = l
        board[pos[l][1][0]][pos[l][1][1]] = l
        
        d1 = move(i, j, *pos[l][1])
        board[pos[l][1][0]][pos[l][1][1]] = 0
        d2 = move(*pos[l][1], *pos[l][0])
        board[pos[l][0][0]][pos[l][0][1]] = 0
        dfs(cnt + d1 + d2, pos[l][0][0], pos[l][0][1], k + 1)
        board[pos[l][0][0]][pos[l][0][1]] = l
        board[pos[l][1][0]][pos[l][1][1]] = l
        vis[l] = False


def solution(_board, r, c):
    global ans, goal, vis, pos, board, m_vis
    
    board = _board
    ans = 987654321
    vis = [False] * 7
    pos = [[] for _ in range(7)]
    m_vis = [[False] * 4 for _ in range(4)]
    
    cnt = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0: continue
            pos[board[i][j]].append((i, j))
            cnt += 1
    
    goal = cnt // 2
    dfs(0, r, c, 0)
    
    return ans + goal * 2
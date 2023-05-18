# 블록 이동.  2023-05-18


from collections import deque


def solution(board):
    
    N = len(board)
    q = deque()
    q.append([0, 0, 0, 1, 0])
    vis = [[0] * N for _ in range(N)]  # 왼쪽 위에있는 칸 기준, - 이면 0b01, | 이면 0b10
    vis[0][0] = 1
    
    ans = 0
    while q:
        i1, j1, i2, j2, cnt = q.popleft()
        if (i2, j2) == (N - 1, N - 1):
            ans = cnt
            break
        
        state = 1 if i1 == i2 else 2  # 1 이면 가로, 2이면 세로
        
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni1, nj1, ni2, nj2 = i1 + di, j1 + dj, i2 + di, j2 + dj
            if not 0 <= ni1 or not 0 <= nj1 or not ni2 < N or not nj2 < N:
                continue
            if board[ni1][nj1] == 1 or board[ni2][nj2] == 1:
                continue
            if vis[ni1][nj1] & state: continue
            vis[ni1][nj1] |= state
            q.append((ni1, nj1, ni2, nj2, cnt + 1))
        
        if state == 1:
            if i1 - 1 >= 0:
                if board[i1 - 1][j1] == 0 and not vis[i2 - 1][j2] & 2 and board[i2 - 1][j2] == 0:
                    vis[i2 - 1][j2] |= 2
                    q.append((i2 - 1, j2, i2, j2, cnt + 1))
                if board[i2 - 1][j2] == 0 and not vis[i1 - 1][j1] & 2 and board[i1 - 1][j1] == 0:
                    vis[i1 - 1][j1] |= 2
                    q.append((i1 - 1, j1, i1, j1, cnt + 1))
            if i1 + 1 < N:
                if board[i1 + 1][j1] == 0 and not vis[i2][j2] & 2 and board[i2 + 1][j2] == 0:
                    vis[i2][j2] |= 2
                    q.append((i2, j2, i2 + 1, j2, cnt + 1))
                if board[i2 + 1][j2] == 0 and not vis[i1][j1] & 2 and board[i1 + 1][j1] == 0:
                    vis[i1][j1] |= 2
                    q.append((i1, j1, i1 + 1, j1, cnt + 1))
        else:
            if j1 - 1 >= 0:
                if board[i2][j2 - 1] == 0 and not vis[i1][j1 - 1] & 1 and board[i1][j1 - 1] == 0:
                    vis[i1][j1 - 1] |= 1
                    q.append((i1, j1 - 1, i1, j1, cnt + 1))
                if board[i1][j1 - 1] == 0 and not vis[i2][j2 - 1] & 1 and board[i2][j2 - 1] == 0:
                    vis[i2][j2 - 1] |= 1
                    q.append((i2, j2 - 1, i2, j2, cnt + 1))
            if j1 + 1 < N:
                if board[i2][j2 + 1] == 0 and not vis[i1][j1] & 1 and board[i1][j1 + 1] == 0:
                    vis[i1][j1] |= 1
                    q.append((i1, j1, i1, j1 + 1, cnt + 1))
                if board[i1][j1 + 1] == 0 and not vis[i2][j2] & 1 and board[i2][j2 + 1] == 0:
                    vis[i2][j2] |= 1
                    q.append((i2, j2, i2, j2 + 1, cnt + 1))
    
    return ans
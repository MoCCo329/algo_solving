# 경주로 건설.  2023-09-02


import heapq, sys


def solution(board):
    INF = sys.maxsize
    N, M = len(board), len(board[0])
    vis = [[[INF] * 4 for __ in range(M)] for _ in range(N)]
    d_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    q = [(0, 0, 0, -1)]
    vis[0][0][0], vis[0][0][1], vis[0][0][2], vis[0][0][3] = 0, 0, 0, 0
    while q:
        cost, i, j, d_before = heapq.heappop(q)
        if cost < vis[i][j][d_before]: continue
        if i == N - 1 and j == M - 1: return cost
        
        for d in range(4):
            if d_before != -1 and d == (d_before + 2) % 4: continue
            di, dj = d_list[d]
            ni, nj = i + di, j + dj
            if ni < 0 or N <= ni or nj < 0 or M <= nj or board[ni][nj] == 1: continue
            new_cost = cost + (100 if (d_before == d or d_before == -1) else 600)
            if vis[ni][nj][d] < new_cost or vis[ni][nj][(d + 2) % 4] + 500 < new_cost or vis[ni][nj][(d + 1) % 4] + 500 < new_cost or vis[ni][nj][(d - 1) % 4] + 500 < new_cost: continue
            vis[ni][nj][d] = new_cost
            vis[ni][nj][(d + 1) % 4] = min(vis[ni][nj][(d + 1) % 4], new_cost + 500)
            vis[ni][nj][(d - 1) % 4] = min(vis[ni][nj][(d - 1) % 4], new_cost + 500)
            vis[ni][nj][(d + 2) % 4] = min(vis[ni][nj][(d + 2) % 4], new_cost)
            heapq.heappush(q, (new_cost, ni, nj, d))
    
    return -1

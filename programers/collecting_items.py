# 아이템 줍기.  2023-05-10


def dfs(i, j, fi, fj, cnt):
    global ans, vis, maps
    
    if i == fi and j == fj:
        ans = min(ans, cnt // 2)
        return
    
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = i + di, j + dj
        if not (0 <= ni <= 100) or not (0 <= nj <= 100): continue
        if vis[ni][nj] == 1 or maps[ni][nj] != 1: continue
        
        vis[ni][nj] = 1
        dfs(ni, nj, fi, fj, cnt + 1)
        vis[ni][nj] = 0


def solution(rectangles, si, sj, fi, fj):
    global ans, vis, maps
    
    maps = [[0] * 101 for _ in range(101)]
    for r in rectangles:
        for i in range(r[0] * 2, r[2] * 2 + 1):
            for j in range(r[1] * 2, r[3] * 2 + 1):
                if maps[i][j] == 2: continue
                
                if i == r[0] * 2 or i == r[2] * 2 or j == r[1] * 2 or j == r[3] * 2:
                    maps[i][j] = 1
                else:
                    maps[i][j] = 2
    
    ans = 2500
    vis = [[0] * 101 for _ in range(101)]
    vis[si * 2][sj * 2] = 1
    dfs(si * 2, sj * 2, fi * 2, fj * 2, 0)
    
    return ans
# 빛의 경로 사이클.  2023-08-27


def solution(grid):
    ans = []
    N = len(grid)
    M = len(grid[0])
    
    d_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    vis = [[[0] * 4 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for d in range(4):
                oi, oj, od = i, j, d
                cnt = 0
                while vis[oi][oj][od] == 0:
                    vis[oi][oj][od] = 1;
                    cnt += 1
                    if grid[oi][oj] == 'S':
                        pass
                    elif grid[oi][oj] == 'L':
                        od = (od - 1) % 4
                    else:
                        od = (od + 1) % 4
                    oi = (oi + d_list[od][0]) % N
                    oj = (oj + d_list[od][1]) % M
                if oi == i and oj == j and od == d and 0 < cnt:
                    ans.append(cnt)
    
    return sorted(ans)
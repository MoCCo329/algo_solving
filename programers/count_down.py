# 카운트 다운.  2023-09-02


def insert(i, j, is_bull):
    global vis

    if vis[i][0] + 1 < vis[j][0]:
        vis[j][0] = vis[i][0] + 1
        vis[j][1] = vis[i][1] + (1 if is_bull else 0)
    elif vis[i][0] + 1 == vis[j][0] and vis[j][1] < vis[i][1] + (1 if is_bull else 0):
        vis[j][1] = vis[i][1] + (1 if is_bull else 0)


def solution(target):
    global vis
    
    INF = target + 1
    vis = [[INF, 0] for _ in range(target + 1)]
    
    vis[0][0] = 0
    for i in range(target + 1):
        if vis[i][0] == INF: continue
        if i + 50 <= target:
            insert(i, i + 50, True)
        for j in range(1, 21):
            if i + j <= target:
                insert(i, i + j, True)
                if i + j * 2 <= target:
                    insert(i, i + j * 2, False)
                    if i + j * 3 <= target:
                        insert(i, i + j * 3, False)
    
    return vis[target]

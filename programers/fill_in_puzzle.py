# 퍼즐 조각 채우기.  2023-10-19


def rotate(arr, N):
    temp = list(arr)
    arr.clear()
    for i, j in temp:
        arr.add((j, N - 1 - i))


def find(i, j, v_set, N, board, want):
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if ni < 0 or N <= ni or nj < 0 or N <= nj or board[ni][nj] != want: continue;
        if (ni, nj) in v_set: continue
        v_set.add((ni, nj))
        find(ni, nj, v_set, N, board, want)


def make_hash(v_set):
    temp = sorted(list(v_set))
    di, dj = temp[0][0], temp[0][1]
    v_set.clear()
    for i in range(len(temp)):
        v_set.add((temp[i][0] - di, temp[i][1] - dj))
    
    
def solution(game_board, table):
    N = len(game_board)
    hm = dict()
    cnt = 0
    vis = [[False] * N for _ in range(N)]
    cnt_to_size = []
    cnt_vis = []
    ans = 0
    
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 1 or vis[i][j]: continue
            temp = []
            v_set = set()
            v_set.add((i, j))
            find(i, j, v_set, N, game_board, 0)
            
            for ii, jj in v_set:
                vis[ii][jj] = True;
            
            make_hash(v_set)
            temp.append(tuple(v_set))
            
            rotate(v_set, N)
            make_hash(v_set)
            temp.append(tuple(v_set))
            
            rotate(v_set, N)
            make_hash(v_set)
            temp.append(tuple(v_set))
            
            rotate(v_set, N)
            make_hash(v_set)
            temp.append(tuple(v_set))
            
            flag = False
            for t in temp:
                if t in hm:
                    cnt_vis[hm[t]] += 1
                    flag = True
                    break
            if not flag:
                for t in temp:
                    hm[t] = cnt
                cnt_to_size.append(len(v_set))
                cnt_vis.append(1)
                cnt += 1
    
    vis = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if table[i][j] == 0 or vis[i][j]: continue
            v_set = set()
            v_set.add((i, j))
            find(i, j, v_set, N, table, 1)
            for ii, jj in v_set:
                vis[ii][jj] = True
            make_hash(v_set)
            v = hm.get(tuple(v_set), -1)
            
            if (v == -1) or (cnt_vis[v] == 0): continue
            ans += cnt_to_size[v]
            cnt_vis[v] -= 1
    
    return ans

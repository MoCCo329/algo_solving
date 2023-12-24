# 공 이동 시뮬레이션.  2023-12-25


d_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_edge(i, j, N, M, d):
    ni, nj = i - d_list[d][0], j - d_list[d][1]
    if not (0 <= ni < N) or not (0 <= nj < M): return True
    return False


def solution(N, M, x, y, queries):
    pos = [x, y, x, y]
    
    for k in range(len(queries) - 1, -1, -1):
        new_pos = set()
        d, n = queries[k]
        
        if is_edge(pos[0], pos[1], N, M, d) or is_edge(pos[2], pos[3], N, M, d):
            if d % 2 == 0:
                pos = [pos[0], pos[1], min(N - 1, pos[2] + d_list[d][0] * n), min(M - 1, pos[3] + d_list[d][1] * n)]
            else:
                pos = [max(0, pos[0] + d_list[d][0] * n), max(0, pos[1] + d_list[d][1] * n), pos[2], pos[3]]
        else:
            pos = [pos[0] + d_list[d][0] * n, pos[1] + d_list[d][1] * n, pos[2] + d_list[d][0] * n, pos[3] + d_list[d][1] * n]
            if pos[2] < 0 or pos[3] < 0: return 0
            if N < pos[0] or M < pos[1]: return 0
            if pos[0] < 0: pos[0] = 0
            if pos[1] < 0: pos[1] = 0
            if N <= pos[2]: pos[2] = N - 1
            if M <= pos[3]: pos[3] = M - 1
    
    return (pos[2] - pos[0] + 1) * (pos[3] - pos[1] + 1)
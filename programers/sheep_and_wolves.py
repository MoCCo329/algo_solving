# 양과 늑대.  2023-08-31


def dfs(i, sheep_cnt, wolf_cnt, avail_node, info, adj_list):
    global ans
    ans = max(ans, sheep_cnt)
    
    for j in adj_list[i]:
        avail_node.add(j)
    
    for j in avail_node:
        if info[j] == 1 and wolf_cnt + 1 < sheep_cnt:
            dfs(j, sheep_cnt, wolf_cnt + 1, avail_node - {j}, info, adj_list)
        elif info[j] == 0:
            dfs(j, sheep_cnt + 1, wolf_cnt, avail_node - {j}, info, adj_list)
    
    for j in adj_list[i]:
        avail_node.remove(j)
    

def solution(info, edges):
    global ans
    
    N = len(info)
    adj_list = [[] for _ in range(N)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
    
    ans = 0
    dfs(0, 1, 0, set(), info, adj_list)
    
    return ans

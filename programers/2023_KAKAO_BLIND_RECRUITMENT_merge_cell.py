# 표 병합 2023 KAKAO BLIND RECRUITMENT  2023-04-11


def find(a):
    if uf[a] == a:
        return a
    
    temp = find(uf[a])
    uf[a] = temp
    for c in hs_list[a]:
        hs_list[temp].add(c)
    hs_list[a].clear()
    
    return uf[a]


def union(a, b):
    for c in hs_list[b]:
        hs_list[a].add(c)
    hs_list[b].clear()
    
    hs_list[a].add(b)
    uf[b] = a


def change(i, j, v):
    idx = i * 50 + j
    p_idx = find(idx)
    v_list[p_idx] = v


def update(v1, v2):
    for idx in range(2500):
        if v_list[idx] == v1:
            v_list[idx] = v2


def merge(i1, j1, i2, j2):
    idx1, idx2 = i1 * 50 + j1, i2 * 50 + j2
    p_idx1, p_idx2 = find(idx1), find(idx2)
    
    if p_idx1 == p_idx2: return
    
    v1, v2 = v_list[p_idx1], v_list[p_idx2]
    v = v1 or v2 if v1 or v2 else ""
    
    union(p_idx1, p_idx2)
    v_list[p_idx1] = v
    v_list[p_idx2] = ""


def unmerge(i, j):
    idx = i * 50 + j
    p_idx = find(idx)
    
    if v_list[p_idx]:
        temp = v_list[p_idx]
        v_list[p_idx] = ""
        v_list[idx] = temp
    
    for c in hs_list[p_idx]:
        uf[c] = c
    hs_list[p_idx].clear()


def pprint(i, j):
    idx = i * 50 + j
    
    p_idx = find(idx)
    
    if v_list[p_idx]:
        ans.append(v_list[p_idx])
    else:
        ans.append("EMPTY")


def solution(commands):
    global ans, uf, hs_list, v_list
    
    ans = []
    uf = [i for i in range(2500)]
    hs_list = [set() for _ in range(2500)]
    v_list = ["" for _ in range(2500)]
    
    for command in commands:
        order, *temp = command.split()
        
        if order == "UPDATE" and len(temp) == 3:
            change(int(temp[0]) - 1, int(temp[1]) - 1, temp[2])
        elif order == "UPDATE":
            update(temp[0], temp[1])
        elif order == "MERGE":
            merge(int(temp[0]) - 1, int(temp[1]) - 1, int(temp[2]) - 1, int(temp[3]) - 1)
        elif order == "UNMERGE":
            unmerge(int(temp[0]) - 1, int(temp[1]) - 1)
        else:
            pprint(int(temp[0]) - 1, int(temp[1]) - 1)
    
    return ans
# 섬 연결하기.  2023-05-14


def solution(n, costs):
    
    def find(i):
        if uf[i] == i: return i
        
        uf[i] = find(uf[i])
        return uf[i]
    
    def union(a, b):
        if a > b:
            uf[b] = a
        else:
            uf[a] = b
    
    uf = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    
    ans = 0
    for cost in costs:
        a = find(cost[0])
        b = find(cost[1])
        
        if a != b:
            ans += cost[2]
            union(a, b)
    
    return ans
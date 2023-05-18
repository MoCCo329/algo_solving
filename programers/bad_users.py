# 불량 사용자.  2023-05-18


def solution(user_id, banned_id):
    global ans
    
    def dfs(i, banned_set):
        global ans
        
        if i == N:
            ans.add(tuple(sorted(list(banned_set))))
            return
        
        L = len(banned_id[i])
        star = 0
        for j in range(L):
            if banned_id[i][j] == '*':
                star += 1
        
        for user in sorted_user_id[L]:
            if user in banned_set: continue
            cnt = 0
            for j in range(L):
                if banned_id[i][j] == user[j]:
                    cnt += 1
            if star + cnt == L:
                banned_set.add(user)
                dfs(i + 1, banned_set)
                banned_set.remove(user)
    
    
    N = len(banned_id)
    sorted_user_id = [[] for _ in range(9)]
    for user in user_id:
        sorted_user_id[len(user)].append(user)
    
    ans = set()
    dfs(0, set())
    
    return len(ans)
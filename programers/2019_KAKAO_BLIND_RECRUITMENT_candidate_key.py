# 후보키 2019 KAKAO BLIND RECRUITMENT  2022-09-19


def solution(relation):
    global cal_list
    
    L = len(relation[0])
    N = len(relation)
    
    def dfs(i, k, L, arr):  # i번째, k개 고르기, L길이
        global cal_list
        
        if i > L:
            return
        for cal in cal_list:
            if set(cal) & set(arr) == set(cal):
                return
        
        if len(arr) == k:
            temp = [tuple(relation[ii][jj] for jj in arr) for ii in range(N)]
            if len(temp) == len(set(temp)):
                cal_list.append(arr[::])
            return
        
        dfs(i + 1, k, L, arr)
        for j in range(i, L):
            dfs(j + 1, k, L, arr + [j])
    
    
    cal_list = []
    for i in range(1, L + 1):
        dfs(0, i, L, [])
        
    ans = len(cal_list)
    
    return ans
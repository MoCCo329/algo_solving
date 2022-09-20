# 양궁대회 2022 KAKAO BLIND RECRUITMENT  2022-09-20


def solution(n, info):
    global ans, ans_list
    
    
    def test():
        for i in range(10, -1, -1):
            if counts[i] > ans_list[i]:
                return True
            if counts[i] < ans_list[i]:
                return False
        return False
    
    
    def dfs(i, cnt, n, score):
        global ans, ans_list
        
        if cnt > n or i > 9:
            return
        
        temp = n - cnt
        counts[10] += temp
        if ans < score or (ans == score and test()):
            ans = score
            ans_list = counts[::]
        counts[10] -= temp

        for j in candi[i]:
            counts[i] = j
            if j:
                if info[i] == 0:
                    dfs(i + 1, cnt + j, n, score + (10 - i))
                else:
                    dfs(i + 1, cnt + j, n, score + (10 - i) * 2)
            else:
                dfs(i + 1, cnt, n, score)
            counts[i] = 0
    

    ans = 0
    ans_list = [0] * 11
    counts = [0] * 11

    candi = []
    for i in range(11):
        candi.append((0, info[i] + 1))
    
    s_a = 0
    for i in range(10):
        s_a -= 10 - i if info[i] else 0
    
    dfs(0, 0, n, s_a)
    
    if ans == 0:
        return [-1]
    else:
        return ans_list
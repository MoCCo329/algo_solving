# 수식 최대화 2020 KAKAO INTERNSHIP  2022-09-16


def solution(ex):
    global ans
    
    def dfs(i, arr):
        global ans
        
        if i == 3:
            ans = max(ans, abs(cal(*arr)))
            return
        
        for j in range(3):
            if v[j]: continue
            v[j] = 1
            next = ['+', '-', '*'][j]
            dfs(i + 1, arr + [next])
            v[j] = 0
    
    
    def cal(*opers):
        cnt = [0] * (len(nums) + 1)
        temp_nums = nums[::]
        
        for oper in opers:
            for idx in oper_dict[oper]:
                temp_cnt = sum(cnt[:idx])
                a, b = temp_nums[idx - 1 - temp_cnt], temp_nums[idx - temp_cnt]
                if oper == '+':
                    temp = a + b
                elif oper == '-':
                    temp = a - b
                elif oper == '*':
                    temp = a * b
                temp_nums[idx - 1 - temp_cnt] = temp
                temp_nums.pop(idx - temp_cnt)
                cnt[idx] += 1
        
        return temp_nums[0]
    
    
    L = len(ex)
    nums = []
    oper_dict = { '+': [], '-': [], '*': [] }
    temp = ''
    
    i = 0
    while i < L:
        if ex[i] in ['+', '-', '*']:
            nums.append(int(temp))
            oper_dict[ex[i]].append(len(nums))
            temp = ''
        else:
            temp += ex[i]
        i += 1
    nums.append(int(temp))
    
    v = [0, 0, 0]
    ans = 0
    dfs(0, [])
    
    return ans
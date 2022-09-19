# 신규 아이디 추천 2021 KAKAO BLIND RECRUITMENT  2022-09-19


def find(num, arr):
    if not arr: return 0
    
    L = len(arr)
    
    start = 0
    end = L - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= num:
            end = mid - 1
        else:
            start = mid + 1
    
    return L - start


def solution(info, query):
    info_dict = { (i, j, k, l) : [] for i in range(3) for j in range(2) for k in range(2) for l in range(2) }
    # java-cpp-python, backend-frontend, junior-senior, pizza-chicken
    
    for inf in info:
        inf = inf.split(' ')
        temp = [0, 0, 0, 0]
        if inf[0] == 'java':
            temp[0] = 1
        elif inf[0] == 'cpp':
            temp[0] = 2
        if inf[1] == 'backend':
            temp[1] = 1
        if inf[2] == 'junior':
            temp[2] = 1
        if inf[3] == 'pizza':
            temp[3] = 1
        
        info_dict[tuple(temp)].append(int(inf[4]))
    
    for key in info_dict.keys():
        info_dict[key].sort()
    
    ans = []
    for quer in query:
        quer = quer.replace('and', '').split('  ')
        temp = quer[-1].split(' ')
        quer[-1] = temp[0]
        quer.append(temp[1])

        if quer[0] == 'java':
            temp = [(1, 0, 0, 0)]
        elif quer[0] == 'cpp':
            temp = [(2, 0, 0, 0)]
        elif quer[0] == '-':
            temp = [(0, 0, 0, 0), (1, 0, 0, 0), (2, 0, 0, 0)]
        else:
            temp = [(0, 0, 0, 0)]
        
        if quer[1] == 'backend':
            for i in range(len(temp)):
                tem = list(temp[i])
                tem[1] = 1
                temp[i] = tuple(tem)
        elif quer[1] == '-':
            for i in range(len(temp)):
                copy = list(temp[i])
                copy[1] = 1
                temp.append(tuple(copy))

        if quer[2] == 'junior':
            for i in range(len(temp)):
                tem = list(temp[i])
                tem[2] = 1
                temp[i] = tuple(tem)
        elif quer[2] == '-':
            for i in range(len(temp)):
                copy = list(temp[i])
                copy[2] = 1
                temp.append(tuple(copy))
        
        if quer[3] == 'pizza':
            for i in range(len(temp)):
                tem = list(temp[i])
                tem[3] = 1
                temp[i] = tuple(tem)
        elif quer[3] == '-':
            for i in range(len(temp)):
                copy = list(temp[i])
                copy[3] = 1
                temp.append(tuple(copy))

        cnt = 0
        for tem in temp:
            cnt += find(int(quer[4]) ,info_dict[tem])
        ans.append(cnt)
    
    return ans
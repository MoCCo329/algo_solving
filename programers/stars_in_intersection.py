# 교점에 별 만들기.  2023-08-27


def solution(line):
    memo = dict()
    flag = True
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    
    for i in range(1, len(line)):
        for j in range(i):
            a = line[i][1] * line[j][2] - line[i][2] * line[j][1]
            b = line[i][0] * line[j][1] - line[i][1] * line[j][0]
            if b == 0 or a % b != 0: continue
            c = line[i][2] * line[j][0] - line[i][0] * line[j][2]
            d = line[i][0] * line[j][1] - line[i][1] * line[j][0]
            if d == 0 or c % d != 0: continue
            X, Y = a // b, c // d
            if Y not in memo: memo[Y] = []
            memo[Y].append(X)
            if flag:
                min_y, max_y, min_x, max_x = Y, Y, X, X
                flag = False
            min_y = min(min_y, Y)
            max_y = max(max_y, Y)
            min_x = min(min_x, X)
            max_x = max(max_x, X)
    
    x_size = max_x - min_x + 1
    y_size = max_y - min_y + 1
    ans = [['.' for _ in range(x_size)] for _ in range(y_size)]
    
    for k, v_list in memo.items():
        for v in v_list:
            ans[max_y - k][v - min_x] = '*'
    
    return ["".join(ans[i]) for i in range(y_size)]
# 14572. 스터디 그룹  2023-06-27


import sys
input = sys.stdin.readline


def get_ans():
    v_union = 0
    v_intersec = 0
    for k in range(K + 1):
        if counts[k] != 0:
            v_union += 1
            if counts[k] == p_cnt:
                v_intersec += 1

    return (v_union - v_intersec) * p_cnt


N, K, D = map(int, input().split())
students = []
prob = []
for i in range(N):
    m, d = map(int, input().split())
    prob.append(list(map(int, input().split())))
    students.append((d, i))
students.sort()

i = 0
j = 0
p_cnt = 1
counts = [0] * (K + 1)

for p in prob[students[0][1]]:
    counts[p] += 1

ans = 0
while j <= i:
    if students[i][0] - students[j][0] <= D:
        ans = max(ans, get_ans())
        i += 1
        if i == N: break
        p_cnt += 1
        for p in prob[students[i][1]]:
            counts[p] += 1
    else:
        p_cnt -= 1
        for p in prob[students[j][1]]:
            counts[p] -= 1
        j += 1

print(ans)
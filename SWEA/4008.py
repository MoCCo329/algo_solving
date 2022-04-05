# 4008. 숫자 만들기 2022-04-05

def f(i, k, p):
    global num_cnt, maxV, minV
    if i == k:  # 완성된 경우
        if p > maxV:
            maxV = p
        if p < minV:
            minV = p
    else:
        next = numb[i]
        if oper[0] > 0:
            oper[0] -= 1
            f(i + 1, k, p + next)
            oper[0] += 1
        if oper[1] > 0:
            oper[1] -= 1
            f(i + 1, k, p - next)
            oper[1] += 1
        if oper[2] > 0:
            oper[2] -= 1
            f(i + 1, k, p * next)
            oper[2] += 1
        if next != 0 and oper[3] > 0:
            oper[3] -= 1
            f(i + 1, k, int(p / next))
            oper[3] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    oper = list(map(int, input().split()))
    numb = list(map(int, input().split()))
    num_cnt = [0] * 10
    for i in range(N):
        num_cnt[numb[i]] += 1

    maxV = -100000000
    minV = 100000000
    f(1, N, numb[0])
    print(f'#{tc} {maxV - minV}')
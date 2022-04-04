def nPr(n, r, k):
    if k == r:

    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                nPr(n, r, k + 1)
                used[i] = 0


def ()


T = int(input())
for tc in range(1, T + 1):
    N = int(input()):
    oper = list(map(int, input().split()))
    numb = list(map(int, input().split()))
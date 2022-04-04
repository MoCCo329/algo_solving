def merge(l, r, L, R):
    global cnt
    if l[-1] > r[-1]:
        cnt += 1

    result = []
    ls = 0
    rs = 0
    while ls < L or rs < R:
        if ls < L and rs < R:
            if l[ls] <= r[rs]:
                result += [l[ls]]
                ls += 1
            else:
                result += [r[rs]]
                rs += 1
        elif ls < L:
            result += l[ls:]
            break
        elif rs < R:
            result += r[rs:]
            break
    return result


def merge_sort(M):
    l = len(M)
    m = l // 2
    if l == 1:
        return M
    return merge(merge_sort(M[:m]), merge_sort(M[m:]), m, l-m)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    print(f'#{tc} {merge_sort(list(map(int, input().split())))[N//2]} {cnt}')
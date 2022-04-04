def charge(i, N, b, cnt):
    global ans

    if i == N:
        if ans > cnt and b >= 0:
            ans = cnt
        return
    elif b < 0:
        return
    elif ans < cnt:
        return
    else:
        charge(i + 1, N, b - 1, cnt)
        charge(i + 1, N, arr[i-1] - 1, cnt + 1)


T = int(input())
for tc in range(1, T+1):
    N, *arr = map(int, input().split())
    ans = N-2
    charge(2, N, arr[0]-1, 0)  # 2번 정류장에서 arr[0]-1 베터리를 가지고 시작
    print(f'#{tc} {ans}')
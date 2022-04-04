T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_arr = sorted(list(map(int, input().split())))
    M_arr = sorted(list(map(int, input().split())))
    ans = 0

    for m in M_arr:
        chk = 0
        low = 0
        high = N - 1
        while low <= high:
            mid = (low + high) // 2
            if N_arr[mid] == m:

                ans += 1
                break
            elif m < N_arr[mid]:
                if chk == 1:
                    break
                else:
                    chk = 1
                    high = mid - 1
            else:
                if chk == 2:
                    break
                else:
                    chk = 2
                    low = mid + 1
    print(f'#{tc} {ans}')
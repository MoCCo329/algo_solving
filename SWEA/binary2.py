T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ''
    for i in range(1, 13):
        if N >= 2**(-i):
            ans += '1'
            N -= 2**(-i)
        else:
            ans += '0'
    ans = ans.rstrip('0')

    if not N:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} overflow')
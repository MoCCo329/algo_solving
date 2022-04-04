def bs(x, P): #이진 검색 횟수를 반환하는 함수
    start = 1
    end = P
    cnt = 1

    while start <= end:
        mid = int((start + end) / 2)
        if mid == x:
            return cnt
        elif mid > x:
            end = mid
            cnt += 1
        else:
            start = mid
            cnt += 1
    return -1


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    Ac = bs(A, P)
    Bc = bs(B, P)

    if Ac > Bc: # A, B 중 작은수를 출력, 같다면 0을 출력
        print(f'#{tc} B')
    elif Ac < Bc:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')
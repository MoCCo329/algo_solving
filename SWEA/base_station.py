T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    didj = [[-1, 0], [0, -1], [1, 0], [0, 1]] # 방향
    abc = {'A' : 1, 'B' : 2, 'C' : 3} # A, B, C 딕셔너리

    for i in range(N):
        for j in range(N): # N*N 순회
            if arr[i][j] in abc: # 기지국을 만나면
                for di, dj in didj: # 각 방향을 따라
                    for k in range(1, abc[arr[i][j]]+1): # 기지국 종류별로 1,2,3칸씩
                        if 0<=i+di*k<N and 0<=j+dj*k<N:
                            arr[i+di*k][j+dj*k] = 'X' # X로 바꾼다

    cnt = 0
    for i in range(N): # 남아있는 H를 센다.
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')
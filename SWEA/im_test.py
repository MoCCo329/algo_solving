T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 지도 크기
    arr = [list(map(int, input().split())) for _ in range(N)] # 지도
    cap_list = [] # 경비 위치 저장 리스트

    for i in range(N): # 경비 위치 찾기
        for j in range(N):
            if arr[i][j] == 2:
                cap_list += [[i, j]]

    didj = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 이동 방향
    for i, j in cap_list: # 모든 경비 위치에서
        for di, dj in didj: # 각 이동방향으로
            k = 1 # k=1부터
            while 0<=i+di*k<N and 0<=j+dj*k<N and arr[i+di*k][j+dj*k] == 0: # 배열안에 존재하고 0이아닌 수를 만나기 전까지
                arr[i+di*k][j+dj*k] = 1 # 0을 1로 바꾼다
                k += 1 # k값을 증가하며 while 반복

    cnt = 0
    for i in range(N): # 남은 0의 개수 세기
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1

    print(f'#{tc} {cnt}')
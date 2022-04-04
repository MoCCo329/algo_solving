def f(i, c, N):
    global ans
    if c == N//2: # 음식1과 음식2에 재료분배가 완료된 경우, 음식점수 차이를 ans에 저장
        food1 = 0
        food2 = 0
        for j in range(N//2):
            for k in range(N//2):
                food1 += arr[food[j]][food[k]]
                food2 += arr[food[j+N//2]][food[k+N//2]]
        ans += [abs(food1 - food2)]
        return
    else: # 재료분배가 덜 된 경우 섞는다
        for j in range(i, N):
            if chk_list[j] == True:
                continue
            else:
                food[c], food[j] = food[j], food[c]
                chk_list[j] = True
                f(j+1, c+1, N)
                food[c], food[j] = food[j], food[c] # 다시 원상복귀 시키며 탐색
                chk_list[j] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    chk_list = [0] * (N+1)
    food = [i for i in range(N)] # 1~N//2까지가 음식1, 나머지는 음식2
    ans = []
    f(0, 0, N)
    print(f'#{tc} {min(ans)}')
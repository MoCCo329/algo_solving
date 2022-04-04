for T in range(1, 11):
    N = int(input())
    box_list = list(map(int, input().split()))
    new_list = [0] * 101

    for height in box_list: # 가로별 상자 개수를 높이별 개수로 전환 idx=0은 무시함 1~100까지만
        for j in range(height+1):
            new_list[j] += 1

    h_sum = 0 # 위쪽 튀어나온 칸들의 합
    l_sum = 0 # 아래쪽 빈 칸들의 합
    h_idx = 100
    l_idx = 0
    while h_sum < N: # N번 행할 때 최고 높이구하기
        h_sum += new_list[h_idx]
        h_idx -= 1
    if h_sum > N: # while문에서 한층 더 내려간 경우 보정
        h_idx += 1
        h_sum -= N

    while l_sum < N: # N번 행할 때 최저 높이구하기
        l_idx += 1
        l_sum += (100 - new_list[l_idx])
    if l_sum > N: # while문에서 한층 더 올라간 경우 보정
        l_idx -= 1
        l_sum = N

    if h_idx == l_idx and h_sum-l_sum == 0: # N번 전에 완료되고 맞아떨어지면 0
        print(f'#{T} 0')
    elif h_idx == l_idx and h_sum-l_sum != 0: # N번 전에 완료됐으나 안맞아떨어지면 1
        print(f'#{T} 1')
    else:
        print(f'#{T} {h_idx - l_idx}') # N번 전에 완료되지 않으면 높이차를 출력
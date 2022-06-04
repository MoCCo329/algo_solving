T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 화덕 크기 N, 피자 수 M
    q = [] # 큐
    M_list = list(map(int, input().split()))

    # 화덕에 N개의 피자 넣기
    idx = 0
    while idx < N:
        q.append([M_list[idx]//2, idx]) # 큐에 [처음치즈양//2, 피자번호-1]로 담긴다.
        idx += 1

    # 화덕 돌리기
    while q: # 화덕에 피자가 있으면 반복
        temp = q.pop(0)
        if temp[0] != 0: # 꺼낸 피자 치즈양이 0이 아니면 //2 해서 다시 넣는다.
            temp[0] = temp[0]//2
            q.append(temp)
        else: # 꺼낸 피자가 0일 때 M_list에 남는 피자가 있으면 넣고, 아니면 0을 넣는다.
            if idx == M:
                pass
            else:
                q.append([M_list[idx]//2, idx])
                idx += 1

    print(f'#{tc} {temp[1]+1}') # 마지막 반복될때의 temp가 마지막 피자를 의미
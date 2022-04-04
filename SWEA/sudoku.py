T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    cnt = 0
    for i in range(9):
        count1 = [0] * 9 # 인덱스가 각각 1~9를 의미하는 count 리스트 생성
        count2 = [0] * 9
        for j in range(9):
            count1[arr[i][j]-1] += 1 # 가로를 훑으며 숫자가 몇번씩 나오는지 count 리스트에 카운팅
            if count1[arr[i][j]-1] == 2: # 2번이상 중복되어 나오면 cnt 에 1 추가
                cnt += 1
                break

            count2[arr[j][i]-1] += 1 # 세로를 훑는다.
            if count2[arr[j][i]-1] == 2:
                cnt += 1
                break

    for i in range(3):
        for j in range(3): # 정사각형을 훑는다.
            count3 = [0] * 9
            for k in range(3):
                for l in range(3):
                    count3[arr[3*i+k][3*j+l]-1] += 1
                    if count3[arr[3*i+k][3*j+l]-1] == 2:
                        cnt += 1
                        break

    if cnt == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
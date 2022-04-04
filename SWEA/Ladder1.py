for T in range(10):
    tc = int(input())
    m = []
    for _ in range(100):
        m = [[0] + list(map(int, input().split())) + [0]] + m # 사다리 양 끝에 0을 붙여 입력을 받으며, m앞에 받는것을 반복해 위아래가 뒤바뀌도록 받는다.

    L = [[i, m[0][i]] for i in range(102) if m[0][i] == 1 or m[0][i] == 2] # L은 (가지를 나타내는 열이 아닌 기둥 열의 인덱스)와 (기둥의 숫자가 1인지 2인지)를 원소로 같는다.
    nL = [0] + [l[0] + 1 for l in L] # nL은 기둥이 아닌 가지를 나타내는 열들의 인덱스로, 기둥 좌우로 가지열이 1개씩 존재하도록 하였다.
    L_idx = [idx for idx, l in enumerate(L) if l[1] == 2][0] # L_idx는 L에 사용할 인덱스이다. 처음 값은 2를 가지는 L의 인덱스이다. list comprehension으로 표현하고 [0]을 붙여 정수로 저장한다.

    k = 0 # 가지의 높이
    while k < 99: # 가지 높이가 100되기 전까지
        if m[k][nL[L_idx]] == 0 and m[k][nL[L_idx+1]] == 0: # 기둥열 좌우 가지열이 0이면 높이 1 증가
            k += 1
        elif m[k][nL[L_idx]] == 1: # 기둥열 왼쪽 가지열의 값이 1이 나온경우 L_idx 1감소
            L_idx -= 1
            k += 1
        else: # 기둥열 오른쪽 가지열의 값이 1이 나온경우 L_idx 1증가
            L_idx += 1
            k += 1

    print(f'#{tc} {L[L_idx][0]-1}')
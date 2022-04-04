# 입력값 받기
N = int(input())
like_list = [0] * (N**2 + 1) # 학생 번호 인덱스에 해당 학생이 좋아하는 사람의 리스트가 담긴다.
arr = [[0]*N for _ in range(N)]
order = []

for _ in range(N**2):
    i, *like = map(int, input().split())
    order += [i]
    like_list[i] = like
    
# 학생 번호를 주면 주어진 조건에 맞춰 arr에 자리배정하는 함수
def f(idx):
    candi_like = [[]]*5 # 인덱스에 해당 인덱스만큼 주변 좋아하는 사람이 있는 [좌표]들이 저장된다.
    candi_blank = [[]]*5 # 주변 빈칸 [[좌표], [좌표], ...] 식으로 저장된다.
    maxV_like = 0 # 주변에 좋아하는 사람수가 가장 많을때 그 값
    maxV_blank = 0 # 주변에 빈칸의 수가 가장 많을때 그 값
    like = like_list[idx] # 해당 학생이 좋아하는 학생들 리스트생성

    # 교실을 훑으며 후보군 찾기
    temp0 = []
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                like_num = 0 # 주변 좋아하는 사람 수 세기
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] in like:
                        like_num += 1
                if like_num == 0: # 좋아하는 사람 수에 따라 temp에 넣기, 행번호 열번호가 작은 순서대로 담긴다.
                    temp0 += [[i, j]]
                elif like_num == 1:
                    temp1 += [[i, j]]
                elif like_num == 2:
                    temp2 += [[i, j]]
                elif like_num == 3:
                    temp3 += [[i, j]]
                else:
                    temp4 += [[i, j]]
                if like_num > maxV_like: # 최대경우일때 maxV 최신화
                    maxV_like = like_num
    candi_like = [temp0, temp1, temp2, temp3, temp4]

    # 찾은 후보군들로 룰에 따라 자리 지정
    if len(candi_like[maxV_like]) > 1: # 옆에 좋아하는 사람이 많이 오도록하는 자리가 없거나 여러개이면
        # 후보군 중 빈칸이 가장 많은곳 찾기
        temp0 = []
        temp1 = []
        temp2 = []
        temp3 = []
        temp4 = []
        for i, j in candi_like[maxV_like]:
            blank_num = 0  # 주변 빈칸 수 세기
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    blank_num += 1
            if blank_num == 0: # 빈칸 수에 따라 temp에 넣기, 행번호 열번호가 작은 순서대로 담긴다.
                temp0 += [[i, j]]
            elif blank_num == 1:
                temp1 += [[i, j]]
            elif blank_num == 2:
                temp2 += [[i, j]]
            elif blank_num == 3:
                temp3 += [[i, j]]
            else:
                temp4 += [[i, j]]
            if blank_num > maxV_blank:
                maxV_blank = blank_num
        candi_blank = [temp0, temp1, temp2, temp3, temp4]

        # 빈칸 수를 따져서 위치 선정
        i, j = candi_blank[maxV_blank][0] # 여러개일 경우 처음 좌표가 행번호, 열번호가 가장 낮다. 한개일 경우 그대로 적용.
        arr[i][j] = idx
    else: # 후보가 한곳인 경우
        i, j = candi_like[maxV_like][0]
        arr[i][j] = idx

# 순서대로 자리배정
for i in order:
    f(i)

# 최종 점수 구하기
score = 0
for i in range(N):
    for j in range(N):
        like = like_list[arr[i][j]]
        cnt = 0 # 주변 좋아하는 사람 수
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] in like:
                cnt += 1
        if cnt == 0:
            continue
        else:
            score += 10**(cnt-1)

# 출력
print(score)
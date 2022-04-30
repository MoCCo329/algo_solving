# 20061 모노미노도미노 2 G2 2022-04-30


N = int(input())
arr1 = [[0] * 4 for _ in range(10)]  # 수직 맵
arr2 = [[0] * 4 for _ in range(10)]  # 수평 맵
ans = 0

for _ in range(N):
    t, i, j = map(int, input().split())

    # 블록 설정
    # arr1에서 i, j 는 arr2에서 j, i
    if t == 1:
        # 1x1
        bArr1 = [[i, j]]
        bArr2 = [[j, i]]
    elif t == 2:
        # arr1에 1x2 arr2에 2x1
        bArr1 = [[i, j], [i, j + 1]]
        bArr2 = [[j, i], [j + 1, i]]
    elif t == 3:
        # arr1에 2x1 arr2에 1x2
        bArr1 = [[i, j], [i + 1, j]]
        bArr2 = [[j, i], [j, i + 1]]
    
    # 블록 내리기
    idxList = [9]
    for k in range(len(bArr1)):
        ii, jj = bArr1[k]
        while ii + 1 < 10 and arr1[ii + 1][jj] == 0:
            ii += 1
        idxList.append(ii)
    ii = min(idxList)
    for k in range(len(bArr1)):
        arr1[ii][bArr1[k][1]] = 1
    if t == 3:
        arr1[ii - 1][bArr1[k][1]] = 1

    idxList = [9]
    for k in range(len(bArr2)):
        ii, jj = bArr2[k]
        while ii + 1 < 10 and arr2[ii + 1][jj] == 0:
            ii += 1
        idxList.append(ii)
    ii = min(idxList)
    for k in range(len(bArr2)):
        arr2[ii][bArr2[k][1]] = 1
    if t == 2:
        arr2[ii - 1][bArr2[k][1]] = 1

    # 점수 확인
    for k in range(6, 10):
        if sum(arr1[k]) == 4:
            ans += 1
            arr1.pop(k)
            arr1 = [[0 for _ in range(4)]] + arr1
        if sum(arr2[k]) == 4:
            ans += 1
            arr2.pop(k)
            arr2 = [[0 for _ in range(4)]] + arr2
    
    # 연한 칸 확인
    for _ in range(2):
        if sum(arr1[5]) != 0:
            arr1.pop()
            arr1 = [[0 for _ in range(4)]] + arr1
        if sum(arr2[5]) != 0:
            arr2.pop()
            arr2 = [[0 for _ in range(4)]] + arr2

print(ans)
tot = 0
for i in range(6, 10):
    tot += sum(arr1[i] + arr2[i])
print(tot)
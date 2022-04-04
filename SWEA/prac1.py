# 버블 정렬

N = int(input()) # 길이
arr = [map(int, input().split())]

for i in range(N-1, -1, -1):
    for j in range(i):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]



# 카운트 정렬

N = int(input()) # 길이
M = int(input()) # 최댓값
arr = [map(int, input().split())]
counts = [0] * M
new_arr = [0] * N

for i in range(N):
    counts[arr[i]] += 1

for i in range(1, M):
    counts[i] += counts[i-1]

for i in range(N):
    counts[arr[i]] -= 1
    new_arr[counts[arr[i]]] = arr[i]


# 선택 정렬

N = int(input())
arr = list(map(int, input().split()))

for i in range(N, 1, -1):
    maxIdx = 0
    for j in range(1, i):
        if arr[maxIdx] < arr[j]:
            maxIdx = j
    arr[maxIdx], arr[i-1] = arr[i-1], arr[maxIdx]

for i in range(N-1):
    minIdx = i
    for j in range(i+1, N):
        if arr[minIdx] < arr[j]:
            minIdx = j
    arr[minIdx], arr[i] = arr[i], arr[minIdx]

# 지그재그 순회

N, M = map(int, input().split())
arr = list(map(int, input().split()) for _ in range(N))

for i in range(N):
    for j in range(M):
        print(arr[i][j + (i%2)*(M-1 - 2*j)])

고지식한 문자열 검색

str1 = input()
str2 = input()
N, M = map(int, input().split())
answer = []

for i in range(N-M):
    cnt = 0
    for j in range(M):
        if str1[i+j] == str2[j]:
            cnt += 1
    if cnt == M:
        answer += str1[i:i+M]

i = j = 0
while i < N and j < M:
    if str1[i] != str2[j]:
        i = i - j + 1
        j = -1
    else:
        i = i + 1
        j = j + 1

if j == M:
    print(str1[i-M:i])
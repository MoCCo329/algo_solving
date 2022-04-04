# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     cnt = [0]*N
#     for i in range(N-1):
#         for j in range(i+1, N):
#             if arr[i] > arr[j]:
#                 cnt[i] += 1
#
#     maxV = cnt[0]
#     for i in range(1, N):
#         if maxV < cnt[i]:
#             maxV = cnt[i]
#     print(f'#{tc} {maxV}')

for T in range(1, int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = [0]*N
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt[i] += 1
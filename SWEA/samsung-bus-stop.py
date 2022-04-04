# for T in range(int(input())):
#     N = int(input())
#     bs = [0] * 5000
#     for i in range(N):
#         A, B = map(int, input().split())
#         for j in range(A-1, B):
#             bs[j] += 1
#
#     c_list = []
#     for i in range(int(input())):
#         c_list += [int(input())]
#
#     print(f'#{T + 1}', end=' ')
#     for i in c_list:
#         print(bs[i-1], end=' ')


for T in range(int(input())):
    N = int(input())
    bs = [0] * 5000
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A-1, B):
            bs[j] += 1

    print(f'#{T+1}', end=' ')
    for i in range(int(input())):
        print(bs[int(input())-1], end=' ')
    print("")
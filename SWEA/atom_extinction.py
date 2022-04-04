# d = {0: (0, 0.5), 1: (0, -0.5), 2: (-0.5, 0), 3: (0.5, 0)}
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     atoms = []
#     for _ in range(N):
#         atoms += [list(map(int, input().split()))]
#
#     ans = 0
#     atoms.sort(key=lambda x: x[1])
#     t = atoms[-1][1] - atoms[0][1]
#     atoms.sort()
#     t = max(t, atoms[-1][0] - atoms[1][0])
#     for _ in range(t):
#         L = len(atoms)
#         pop_list = []
#         for i in range(L):  # 이동
#             di, dj = d[atoms[i][2]]
#             atoms[i][0] += di
#             atoms[i][1] += dj
#
#             for j in range(i+1, L):  # 좌표 중간에 만난경우 찾기
#                 if (atoms[i][0], atoms[i][1]) == (atoms[j][0], atoms[j][1]) and atoms[i][2] // 2 == atoms[j][2] and atoms[i][2] != atoms[j][2]:
#                     pop_list += [i, j]
#
#         pop_list.sort(reverse=True)
#         for idx in pop_list:  # 좌표 중간에서 소멸
#             ans += atoms[idx][3]
#             atoms.pop(idx)
#
#         chk = 1
#         L = L - len(pop_list)
#         atoms.sort()
#         for i in range(L-2,-1,-1):  # 겹치는 경우 빼기
#             if (atoms[i][0], atoms[i][1]) == (atoms[i+1][0], atoms[i+1][1]):
#                 chk += 1
#             else:
#                 if chk != 1:
#                     for _ in range(chk):
#                         ans += atoms[i+1][3]
#                         atoms.pop(i+1)
#                     chk = 1
#         if chk != 1:
#             for _ in range(chk):
#                 ans += atoms[0][3]
#                 atoms.pop(0)
#
#     print(f'#{tc} {ans}')



d = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3: (1, 0)}

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = []
    for _ in range(N):
        atoms += [list(map(int, input().split()))]

    while L > 1:
        ex_atoms = set()
        dis_atoms = set()
        for i in range(L):  # 이동
            di, dj = d[atoms[i][2]]
            atoms[i][0] += di
            atoms[i][1] += dj
            if atoms[i][0] < -1000 or atoms[i][0] > 1000 or atoms[i][1] < -1000 or atoms[i][1] > 1000:
                dis_atoms.add(i)

                for j in range(i+1, L):
                    if not j in dis_atoms and not j in ex_atoms:
                        if atoms[i][0] == atoms[j][0] and atoms[i][1] == atoms[j][1] and atoms[i][2] // 2 == atoms[j][2] // 2 and atoms[i][2] != atoms[j][2]:
                            ex_atoms.update([i, j])

        for i in range(N):
            if not i in dis_atoms and not i in ex_atoms:
                chk = 0
                for j in range(i+1, L):
                    if j not in dis_atoms and not j in ex_atoms:
                        if atoms[i][0] == atoms[j][0] and atoms[i][1] == atoms[j][1]:
                            ex_atoms.add(j)
                            chk = 1
                if chk:
                    ex_atoms.add(i)

    ans = 0
    temp =
    for i in
        ans += atoms[i][3]
    print(f'#{tc} {ans}')
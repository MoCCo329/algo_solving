# 1251. 하나로 2022-04-06

def find_set(x):
    while x != MST[x]:
        x = MST[x]
    return x


def union_set(x, y):
    MST[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())

    edge = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            if i != j:
                edge.append( (((x_list[i] - x_list[j]) ** 2 + (y_list[i] - y_list[j]) ** 2) * E, i, j) )
    edge.sort()

    MST = [i for i in range(N)]
    cnt = 0
    ans = 0
    for w, u, v in edge:
        if find_set(u) != find_set(v):
                cnt += 1
                ans += w
                union_set(u, v)
                if cnt == N - 1:
                    break

    print(f'#{tc} {ans:.0f}')
# 2162. 선분 그룹  2023-06-01


def find(a):
    if uf[a] != a:
        uf[a] = find(uf[a])
    return uf[a]


def union(a, b):
    global group

    A, B = find(a), find(b)
    if A == B: return

    if lank[A] > lank[B]:
        uf[B] = A
        lank[A] += lank[B]
    else:
        uf[A] = B
        lank[B] += lank[A]
    group -= 1


def ccw(p1, p2, p3):
    cross = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1]
    if cross == 0: return 0
    elif cross < 0: return -1
    else: return 1


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
uf = [i for i in range(N)]
lank = [1] * N
group = N

for i in range(1, N):
    for j in range(i):
        p1, p2, p3, p4 = points[i][:2], points[i][2:], points[j][:2], points[j][2:]
        m1, m2 = ccw(p1, p2, p3) * ccw(p1, p2, p4), ccw(p3, p4, p1) * ccw(p3, p4, p2)
        if m1 == 0 == m2:
            if p1 > p2: p1, p2 = p2, p1
            if p3 > p4: p3, p4 = p4, p3
            if p2 < p3 or p4 < p1: continue
        elif m1 > 0 or m2 > 0: continue

        union(i, j)

print(group)
print(max(lank))
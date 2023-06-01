# 2162. 선분 그룹  2023-06-01


def find(a):
    if uf[a] == a: return a

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


def ccw(x1, y1, x2, y2, x3, y3):
    cross = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    if cross == 0: return 0
    elif cross < 0: return -1
    else: return 1


def is_large(a, b):  # b가 a보다 오른쪽 점인가
    if a[0] == b[0]: return a[1] <= b[1]
    return a[0] <= b[0]


def align(p1, p2):
    if not is_large(p1, p2):
        p1[0], p1[1], p2[0], p2[1] = p2[0], p2[1], p1[0], p1[1]


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
uf = [i for i in range(N)]
lank = [1] * N
group = N

for i in range(1, N):
    for j in range(i):
        p1, p2, p3, p4 = points[i][:2], points[i][2:], points[j][:2], points[j][2:]
        m1, m2 = ccw(*p1, *p2, *p3) * ccw(*p1, *p2, *p4), ccw(*p3, *p4, *p1) * ccw(*p3, *p4, *p2)

        if m1 == 0 == m2:
            align(p1, p2), align(p3, p4)
            if not is_large(p3, p2) or not is_large(p1, p4):
                continue
        if m1 > 0 or m2 > 0: continue

        union(i, j)

print(group)
print(max(lank))
# 1708. 볼록 껍질  2023-06-04


import sys
input = sys.stdin.readline


def ccw(a, b, c):
    return a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - b[0] * a[1] - c[0] * b[1] - a[0] * c[1] > 0


def convex_hull():
    stack = []
    for dot in dots:
        while len(stack) >= 2 and not ccw(stack[-2], stack[-1], dot):
            stack.pop()
        stack.append(dot)

    return len(stack)


N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]
dots.sort()
stack = []

ans = convex_hull()
dots.sort(reverse=True)
ans += convex_hull() - 2
print(ans)
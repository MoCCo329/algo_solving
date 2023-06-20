# 7420. 맹독 방벽  2023-06-20


import sys, math
input = sys.stdin.readline


def comp(x):
    if x[1] == pivot[1]: return -sys.maxsize
    return -(x[0] - pivot[0]) / (x[1] - pivot[1])


def ccw(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1])


N, L = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(N)]

dots.sort(key=lambda x: (x[1], x[0]))
pivot = dots.pop(0)
dots.sort(key=comp)

i = N - 2
last_decline = comp(dots[-1])
while 0 <= i and comp(dots[i]) == last_decline:
    if pivot[0] <= dots[i][0]: break
    i -= 1

if i < 0:
    dots = [dots[-1]]
else:
    dots = dots[:i + 1] + dots[i + 1:][::-1]
dots.append(pivot)

stack = [pivot]
for dot in dots:
    if len(stack) < 2:
        stack.append(dot)
    else:
        while len(stack) >= 2 and ccw(stack[-2], stack[-1], dot) < 0:
            stack.pop()
        stack.append(dot)

ans = 2 * L * math.pi
for i in range(len(stack)):
    ans += math.pow((stack[i - 1][0] - stack[i][0]) ** 2 + (stack[i - 1][1] - stack[i][1]) ** 2, 0.5)

print(round(ans))
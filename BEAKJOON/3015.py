# 3015. 오아시스 재결합  2023-03-12


N = int(input())
stack = []
ans = 0

for i in range(N):
    n = int(input())

    count = 1
    while stack and stack[-1][0] <= n:
        ans += stack[-1][1]
        if stack[-1][0] == n:
            count += stack[-1][1]
        stack.pop()

    if stack:
        ans += 1

    stack.append((n, count))

print(ans)
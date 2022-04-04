def find_cubic_root(N):
    for i in range(1, N+1):
        ans = i**3
        if ans > N:
            return -1
        elif ans == N:
            return i

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {find_cubic_root(int(input()))}')
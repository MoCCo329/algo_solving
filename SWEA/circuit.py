T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cq = list(map(int, input().split()))
    rear = 0

    for _ in range(M):
        rear = (rear + 1) % N

    print(f'#{tc} {cq[rear]}')
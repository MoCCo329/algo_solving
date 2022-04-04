def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p >= 1 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def sum_p(n):
    sum = 0
    while n > 0:
        sum += tree[n]
        n = n // 2
    return sum

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    last = 0
    arr = map(int, input().split())
    for n in arr:
        enq(n)
    print(f'#{tc} {sum_p(last//2)}')
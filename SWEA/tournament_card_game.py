def f(i, j):
    if i == j:
        return i
    else:
        left = f(i, (i+j)//2)
        right = f((i+j)//2+1, j)
        return rsp(left, right)

def rsp(A, B):
    if (arr[B] == 1 and arr[A] == 3) or arr[B]-arr[A] == 1:
        return B
    else:
        return A

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    print(f'#{tc} {f(1, N)}')
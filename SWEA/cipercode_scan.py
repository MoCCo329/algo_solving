import sys
sys.stdin = open('1242input.txt', 'r')

ciper = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

def f(code):
    bi = []
    for i in range(8):
        temp = code[i*7:(i+1)*7]
        for j in range(10):
            if ciper[j] == temp:
                bi += [j]
                break
        else:
            return 0
    return bi


def erase(i, j, k, N):
    while i < N and arr[i][j-1] != '0':
        for l in range(j - 56 // 4 * k - 1, j):
            arr[i][l] = '0'
        i += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    codes = []
    result = 0

    for i in range(N):
        for j in range(M - 1, 6, -1):
            if arr[i][j] != '0':
                for k in range(1, 6):
                    temp = ''.join([f'{int(x, 16):04b}' for x in ''.join(arr[i][:j + 1])]).rstrip('0')[-56 * k::k]
                    t = f(temp)
                    if t:
                        codes += [t]
                        erase(i, j+1, k, N)
                        break
                break

    for code in codes:
        if (sum(code[::2]) * 3 + sum(code[1::2])) % 10 == 0:
            result += sum(code)

    print(f'#{tc} {result}')

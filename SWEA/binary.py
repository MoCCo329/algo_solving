T = int(input())
for tc in range(1, T+1):
    N, h = map(str, input().split())
    bi = ''.join([f'{int(x, 16):04b}' for x in h])
    print(f'#{tc} {bi}')
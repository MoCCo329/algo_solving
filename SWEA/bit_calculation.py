T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = ''.join([f'{int(x, 16):04b}' for x in input()])
    print(f'#{tc}', *[int(n[i*7:(i+1)*7], 2) for i in range(len(n)//7)])
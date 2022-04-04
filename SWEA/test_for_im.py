T = int(input())
for tc in range(1, T + 1):
    X, Y = map(int, input().split())

    h = ((X+Y) - (X**2 + Y**2 - X*Y)**(0.5)) / 6

    print('#{} {:.6f}'.format(tc, (X-2*h)*(Y-2*h)*h))
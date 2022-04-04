for T in range(int(input())):
    num = int(input())
    n = [2, 3, 5, 7, 11]
    indices = [0] * 5

    for i in range(5):
        while num % n[i] == 0:
            num /= n[i]
            indices[i] += 1

    print(f'#{T+1}', end=' ')
    print(*indices)
n_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for tc in range(1, T+1):
    sharp, case_num = input().split()
    counts = [0] * 10

    arr = list(input().split())
    for word in arr:
        for i in range(10):
            if n_list[i] == word:
                counts[i] += 1

    print(f'#{tc}')
    for i in range(10):
        for _ in range(counts[i]):
            print(f'{n_list[i]}', end=' ')
    print()
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    counts = [0] * len(str1)

    for i in range(len(str1)):
        for char in str2:
            if str1[i] == char:
                counts[i] += 1

    max_char = counts[0]
    for c in counts:
        if max_char < c:
            max_char = c

    print(f'#{tc} {max_char}')
c = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    code = ''
    for line in arr:  # 코드 찾아 넣기
        for i in range(len(line)-1, -1, -1):
            if line[i] == '1':
                code = ''.join(line[i-55:i+1])
                break
        if code:
            break

    b = [c.index(''.join(code[i*7:(i+1)*7])) for i in range(8)]  # 코드를 숫자로 변환
    chk = 0
    for i in range(8):  # 코드 검증
        if i%2 == 0:
            chk += int(b[i])*3
        else:
            chk += int(b[i])
    if chk % 10 == 0:
        print(f'#{tc} {sum(b)}')
    else:
        print(f'#{tc} 0')
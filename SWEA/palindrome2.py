for tc in range(1, 11):
    tc = int(input())
    arr = [input() for _ in range(100)]
    answer = 0

    for i in range(100): # 가로
        for j in range(100):
            for k in range(100-j, 0, -1):
                for l in range(k//2):
                    if arr[i][j+l] == arr[i][j+k-1-l]:
                        pass
                    else:
                        break
                else: # for문 잘 수행되면 답저장
                    for l in range(k):
                        if answer < k:
                            answer = k

    for j in range(100): # 세로
        for i in range(100):
            for k in range(100-i, 0, -1):
                for l in range(k//2):
                    if arr[i+l][j] == arr[i+k-1-l][j]:
                        pass
                    else:
                        break
                else:
                    for l in range(k):
                        if answer < k:
                            answer = k

    print(f'#{tc} {answer}')
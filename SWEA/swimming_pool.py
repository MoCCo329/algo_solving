def f(M, ans):
    global answer
    if M > 11:
        answer += [ans]
    else:
        # 1일이용권
        f(M+1, ans + plan[M] * arr[0])
        # 1달 이용권
        f(M+1, ans + arr[1])
        # 3달 이용권
        f(M+3, ans + arr[2])

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    answer = [arr[3]]
    f(0, 0)

    print(f'#{tc} {min(answer)}')
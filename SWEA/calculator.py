for tc in range(1, 11):
    N = int(input())
    infix = input()
    postfix = ''
    stack = [0] * N
    top = -1
    icp = {'+': 1, '*': 2}  # 연산자 우선순위
    for i in range(N):
        if '0' <= infix[i] <= '9':  # 피연산자인 경우
            postfix += infix[i]
        else:  # 연산자인 경우
            while top > -1 and icp[stack[top]] >= icp[infix[i]]:  # stack[top] 우선순위가 같거나 높으면  pop
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = infix[i]
    while top > -1:
        postfix += stack[top]
        top -= 1

# 후위연산자 계산
    op1 = 0
    op2 = 0
    stack = [0] * len(postfix)
    for i in range(len(postfix)):
        if postfix[i] == '+': # +일 때
            op2 = int(stack[top])
            top -= 1
            op1 = int(stack[top])
            top -= 1

            top += 1
            stack[top] = op1 + op2

        elif postfix[i] == '*': # *일 때
            op2 = int(stack[top])
            top -= 1
            op1 = int(stack[top])
            top -= 1

            top += 1
            stack[top] = op1 * op2

        else: # 숫자일 때
            top += 1
            stack[top] = int(postfix[i])

    print(f'#{tc} {stack[0]}')
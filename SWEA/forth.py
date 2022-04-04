T = int(input())
for tc in range(1, T+1):
    ex = list(map(str, input().split()))
    size = len(ex)
    stack = [0] * size
    top = -1
    op1 = 0
    op2 = 0

    for i in range(size):
        if ex[i] in ['+', '*', '/', '-']:
            if 1<=top:
                op2 = int(stack[top])
                top -= 1
                op1 = int(stack[top])
                top -= 1

                top += 1
                # stack[top] = int(eval(f'{op1} {ex[i]} {op2}'))
                if ex[i] == '+':
                    stack[top] = op1 + op2
                elif ex[i] == '*':
                    stack[top] = op1 * op2
                elif ex[i] == '/':
                    stack[top] = op1 // op2
                else:
                    stack[top] = op1 - op2
            else:
                print(f'#{tc} error')
                break

        elif ex[i] == '.':
            if top == 0:
                print(f'#{tc} {stack[top]}')
            else:
                print(f'#{tc} error')
                break

        else:
            top += 1
            stack[top] = ex[i]
T = int(input())
for tc in range(1, T+1):
    a = input()
    size = len(a)
    stack = [''] * size
    top = 0
    bracket = {']' : 0, '}' : 0, ')' : 0, '[' : ']', '{' : '}', '(' : ')'}
    check = 0

    for i in range(size):
        if a[i] in bracket:
            if bracket[a[i]] != 0: # 괄호가 열리는 경우
                stack[top] = bracket[a[i]]
                top += 1
            else:
                if stack[top-1] == a[i]: # 제대로 닫히는 경우
                    top -= 1
                else: # 닫히는 괄호가 먼저 오거나 잘못 오는 경우
                    check = 1
                    break

    if top == 0 and check != 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
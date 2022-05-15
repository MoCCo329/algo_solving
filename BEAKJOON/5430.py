# 5430 G5 AC 2022-05-15


T = int(input())
for tc in range(1, T + 1):
    P = list(input())
    N = int(input())
    s = input()
    ans = 0
    if N > 0:
        s = list(s.lstrip('[').rstrip(']').split(','))

    front = 0
    rear = 0
    reverse = 0
    for f in P:
        if f == 'R':
            reverse += 1
        else:
            if N == 0:
                ans = 'error'
                break
            else:
                N -= 1
                if reverse % 2 == 0:
                    front += 1
                else:
                    rear -= 1

    # print(front, rear, reverse)
    if rear != 0:
        s = s[front:rear]
    else:
        s = s[front::]

    if reverse % 2 == 1 and N != 0:
        s.reverse()

    if ans:
        print(ans)
    elif N == 0:
        print('[]')
    else:
        print('[' + ','.join(s) + ']', sep='')
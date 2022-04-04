# def eraser(word):
#     for i in range(len(word)-1):
#         if word[i] == word[i+1]:
#             word.pop(i)
#             word.pop(i+1)
#         return eraser(word)
#     else:
#         return len(word)
#
# T = int(input())
# for tc in range(1, T+1):
#     word = input()
#
#     print(f'#{tc} {eraser(word)}')


# T = int(input())
# for tc in range(1, T+1):
#     word = list(input())
#
#     i = 0
#     while i < len(word)-1:
#         if word[i] == word[i+1]: # 같으면
#             word.pop(i+1) # 뒤에꺼 빼고
#             word.pop(i) # 앞에꺼 빼고
#             i = 0 # i 초기화
#         else:
#             i += 1
#
#     print(f'#{tc} {len(word)}')

T = int(input())
for tc in range(1, T+1):
    word = input()
    size = len(word)
    stack = [''] * size
    stack[0] = word[0]
    top = 0

    for i in range(1, size):
        top += 1
        if stack[top-1] == word[i]:
            top -= 2
        else:
            stack[top] = word[i]

    print(f'#{tc} {top+1}')
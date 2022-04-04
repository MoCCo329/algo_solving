# T = int(input())
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#
#     # for i in range(len(str2)-len(str1)):   # 인덱싱
#     #     if str2[i:i+len(str1)] == str1:
#     #         print(f'#{tc} 1')
#     #         break
#     # else:
#     #     print(f'#{tc} 0')
#
#     answer = 0
#     for i in range(len(str2)-len(str1)+1):   # for문 사용
#         cnt = 0
#         for j in range(len(str1)):
#             if str1[j] == str2[i+j]:
#                 cnt += 1
#
#         if cnt == len(str1):
#             answer += 1
#
#     print(f'#{tc} {answer}')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]

    lth = 1 # 고구마 줄기 길이
    num = arr[0] # 줄기에 달린 고구마 수
    ans_list = [1, 0] # 긴 줄기의 길이, 거기에 달린 고구마 수
    cnt = 0 # 긴 줄기 개수

    for i in range(N):
        if arr[i] < arr[i+1]: # 다음것이 더 크면 줄기길이 증가, 고구마수 추가
            lth += 1
            num += arr[i+1]
        elif lth > 1: # 긴 줄기가 끝났을 때, 기존 줄기보다 더 길면 바꾼다.
            if ans_list[0] < lth:
                ans_list[0], ans_list[1] = lth, num
            elif ans_list[0] == lth and ans_list[1] < num:# 길이는 같은데 고구마가 더 많으면 바꾼다.
                ans_list[1] = num
            cnt += 1
            num = arr[i+1]
            lth = 1
        else:
            num = arr[i + 1]
            lth = 1

    print(f'#{tc} {cnt} {ans_list[1]}')
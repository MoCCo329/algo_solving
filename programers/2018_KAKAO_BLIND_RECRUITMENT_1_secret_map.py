# [1차] 비밀지도 2018 KAKAO BLIND RECRUITMENT  2022-06-10


def solution(n, arr1, arr2):
    
    temp_arr1 = []
    for num in arr1:
        temp_arr1.append(list('{0:b}'.format(num).zfill(n)))
    temp_arr2 = []
    for num in arr2:
        temp_arr2.append(list('{0:b}'.format(num).zfill(n)))
    
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            answer[i][j] = "#" if (int(temp_arr1[i][j]) | int(temp_arr2[i][j])) else " "

    for i in range(n):
        answer[i] = ''.join(answer[i])
    
    return answer
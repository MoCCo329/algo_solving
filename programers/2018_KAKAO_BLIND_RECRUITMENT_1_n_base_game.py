# [1차] n진수 게임 2018 KAKAO BLIND RECRUITMENT  2022-06-19


num_change = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
              13: 'D', 14: 'E', 15: 'F'}

def solution(n, t, m, p):
    def change(n, now):
        ans = []
        temp_num = now
        while temp_num >= 1:
            ans = [num_change[temp_num % n]] + ans
            temp_num = temp_num // n
        return ans

    ans_list = ['0']
    now = 1
    while len(ans_list) < (m * t + p):
        ans_list += change(n, now)
        now += 1

    answer = [ans_list[i * m + p - 1] for i in range(t)]

    return ''.join(answer)
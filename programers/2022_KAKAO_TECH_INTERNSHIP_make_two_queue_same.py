# 두 큐 합 같게 만들기 2022 KAKAO TECH INTERNSHIP  2022-09-07


from collections import deque


def solution(queue1, queue2):
    N = len(queue1)
    q1 = deque(queue1)
    q2 = deque(queue2)
    tot = sum(queue1)
    target = sum([*queue1, *queue2]) // 2

    for cnt in range(2 * N + 10):
        if tot == target:
            return cnt
        elif tot > target:
            temp = q1.popleft()
            tot -= temp
            q2.append(temp)
        else:
            temp = q2.popleft()
            tot += temp
            q1.append(temp)

    return -1
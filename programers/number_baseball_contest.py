# 숫자 타자 대회.  2023-04-21


def cal_cost(a, b):
    maps = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]

    ai, aj, bi, bj = 0, 0, 0, 0
    for i in range(4):
        for j in range(3):
            if maps[i][j] == a:
                ai, aj = i, j
            if maps[i][j] == b:
                bi, bj = i, j

    return 2 * (abs(ai - bi) + abs(aj - bj)) - min(abs(ai - bi), abs(aj - bj))


def solution(numbers):
    before = dict()
    before[(1 << 4) | (1 << 6)] = 0
    for number in numbers:
        number = int(number)
        new = dict()

        for bit, cost in before.items():
            if bit & (1 << number):
                new[bit] = min(new[bit], cost + 1) if new.get(bit, -1) != -1 else cost + 1
                continue

            for i in range(10):
                if (i == number) or not (bit & (1 << i)): continue

                new_cost = cost + cal_cost(i, number)
                new_bit = bit ^ (1 << i) | (1 << number)
                new[new_bit] = min(new[new_bit], new_cost) if new.get(new_bit, -1) != -1 else new_cost

        before = new

    ans = 1000000
    for cost in before.values():
        ans = min(ans, cost)

    return ans
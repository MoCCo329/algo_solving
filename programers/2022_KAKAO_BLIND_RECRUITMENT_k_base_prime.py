# k진수에서 소수 개수 구하기 2022 KAKAO BLIND RECRUITMENT  2022-09-12


def solution(n, k):
    def conv(num, base):
        res = ''
        while num >= 1:
            res = str(num % base) + res
            num //= base
        return res

    def test_pri(num):
        for n in range(2, int(num ** 0.5) + 1):
            if not num % n:
                return False
        else:
            return True

    ans = 0
    for num in conv(n, k).split('0'):
        try:
            num = int(num)
            if num > 1 and test_pri(num):
                ans += 1
        except:
            continue

    return ans
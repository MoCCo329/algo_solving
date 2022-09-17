# 문자열 압축 2020 KAKAO BLIND RECRUITMENT  2022-09-17


def solution(s):
    def test(n, L):
        new_s = [s[n * i:n * i + n] for i in range(L // n)] + ['.']
        ans = L
        cnt = 0
        for i in range(1, len(new_s)):
            if new_s[i - 1] == new_s[i]:
                cnt += 1
            else:
                if cnt:
                    ans = ans - n * cnt + len(str(cnt + 1))
                    cnt = 0
        return ans
        
    
    L = len(s)
    ans = L
    for i in range(1, L // 2 + 1):
        if i > ans:
            break
        ans = min(ans, test(i, L))
    
    return ans
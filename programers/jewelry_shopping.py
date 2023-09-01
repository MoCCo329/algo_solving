# 보석 쇼핑.  2023-09-01


def solution(gems):
    L = 0
    gem_dict = {}
    for gem in gems:
        if gem not in gem_dict:
            gem_dict[gem] = L
            L += 1
    
    counts = [0] * L
    c_cnt = 0
    ans = [1, len(gems)]
    
    l, r = 0, 0
    while r < len(gems) or c_cnt == L:
        if c_cnt < L:
            counts[gem_dict[gems[r]]] += 1
            if counts[gem_dict[gems[r]]] == 1:
                c_cnt += 1
            r += 1
        else:
            counts[gem_dict[gems[l]]] -= 1
            if counts[gem_dict[gems[l]]] == 0:
                c_cnt -= 1
            l += 1
        if c_cnt == L:
            ans_before = ans[1] - ans[0] + 1
            if r - l < ans_before:
                ans = [l + 1, r]
    
    return ans

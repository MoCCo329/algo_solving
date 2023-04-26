# 연속된 부분 수열의 합.  2023-04-26


def solution(arr, k):
    N = len(arr)
    
    r = 0
    tot = arr[0]
    ans = [0, N - 1]
    
    for l in range(N):
        while r < N - 1 and tot < k:
            r += 1
            tot += arr[r]
        
        if tot == k:
            if ans[1] - ans[0] > r - l:
                ans = [l, r]
        
        tot -= arr[l]
    
    return ans
# 소수 찾기.  2022-12-13


### Python

def solution(n):
    p_set = set()
    ans = 0
    for i in range(2, n + 1):
        if i in p_set:
            continue
        
        ans += 1
        temp = i
        while temp <= n:
            p_set.add(temp)
            temp += i
    
    return ans


### JS

# function solution(n) {
    
#     const pSet = new Set()
#     let ans = 1
    
#     pSet.add(2)
#     for (let i = 3; i <= n; i += 2) {
#         if (pSet.has(i)) continue
        
#         ans += 1
#         temp = i
#         while (temp <= n) {
#             pSet.add(temp)
#             temp += i
#         }
#     }
    
#     return ans
# }


### Java

# class Solution {
#     public int solution(int n) {
        
#         int ans = 1;
#         for (int i = 3; i <= n; i = i + 2) {
#            if (primeTest(i)) ans += 1;
#         }
        
#         return ans;
#     }
    
#     public boolean primeTest(int n) {
#         for (int i = 2; i <= (int) Math.sqrt(n); i++) {
#             if (n % i == 0) return false;
#         }
#         return true;
#     }
# }
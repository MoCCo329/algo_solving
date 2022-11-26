# 콜라 문제  2022-11-26


### Python

def solution(a, b, n):
    ans = 0
    
    while n >= a:
        ans += n // a * b
        n = n // a * b + n % a
    
    return ans


### JS

# function solution(a, b, n) {
#     let ans = 0;
    
#     while (n >= a) {
#         ans += Math.floor(n / a) * b
#         n = Math.floor(n / a) * b + n % a
#     }
    
#     return ans
# }


### Java

# class Solution {
#     public int solution(int a, int b, int n) {
#         int ans = 0;
        
#         while (n >= a) {
#             ans += (int) Math.floor(n / a) * b;
#             n = (int) Math.floor(n / a) * b + n % a;
#         }

#         return ans;
#     }
# }
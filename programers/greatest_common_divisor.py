# 최대공약수와 최소공배수.  2022-12-12


### Python

def solution(n, m):
    a, b = max(n, m), min(n, m)
    while b >= 1:
        a, b = b, a % b
    
    return [a, n * m / a]


### JS

# function solution(n, m) {
#     let a = Math.max(n, m)
#     let b = Math.min(n, m)
    
#     while (b >= 1) {
#         const temp = b
#         b = a % b
#         a = temp
#     }
    
#     return [a, n * m / a]
# }


### Java

# class Solution {
#     public int[] solution(int n, int m) {
#         int a = Math.max(n, m);
#         int b = Math.min(n, m);
        
#         while (b >= 1) {
#             int temp = b;
#             b = a % b;
#             a = temp;
#         }
        
#         return new int[] {a, n * m / a};
#     }
# }
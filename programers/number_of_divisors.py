# 약수의 개수와 덧샘


### Python

def solution(left, right):
    ans = 0
    
    for num in range(left, right + 1):
        temp = 0
        for n in range(1, int(num ** 0.5) + 1):
            if num % n == 0:
                if n ** 2 == num:
                    temp += 1
                else:
                    temp += 2
        
        if temp % 2:
            ans -= num
        else:
            ans += num
    
    return ans


### JS

# function solution(left, right) {
#     let ans = 0
#     const getDivisor = (num) => {
#         let ans = 0
#         const end = Math.floor(Math.pow(num, 0.5))
        
#         for (let i = 1; i <= end; i++) {
#             if (num % i === 0) {
#                 if (Math.pow(i, 2) === num) {
#                     ans += 1
#                 } else {
#                     ans += 2
#                 }
#             }
#         }
#         return ans
#     }
    
#     for (let i = left; i <= right; i++) {
#         if (getDivisor(i) % 2) {
#             ans -= i
#         } else {
#             ans += i
#         }
#     }
#     return ans
# }


### Java

# class Solution {
#     public int getDivisor(int num) {
#         int ans = 0;
#         int end = (int) Math.floor(Math.sqrt(num));
        
#         for (int i = 1; i <= end; i++) {
#             if (num % i == 0) {
#                 if (Math.pow(i, 2) == num) {
#                     ans += 1;
#                 } else {
#                     ans += 2;
#                 }
#             }
#         }
#         return ans;
#     }
    
#     public int solution(int left, int right) {
#         int ans = 0;
        
#         for (int i = left; i <= right; i++) {
#             if (getDivisor(i) % 2 == 0) {
#                 ans += i;
#             } else {
#                 ans -= i;
#             }
#         }
        
#         return ans;
#     }
# }
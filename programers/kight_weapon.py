# 기사단원의 무기  2022-11-23


### Python

def solution(number, limit, power):
    ans = 0
    
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** (1/2)) + 1):
            if i % j == 0:
                cnt += 1
                if j ** 2 != i:
                    cnt += 1
            if cnt > limit:
                ans += power
                break
        else:
            ans += cnt
    
    return ans


### JS

# function solution(number, limit, power) {
#     let ans = 0;
    
#     for (let i = 1; i <= number; i++) {
#         let cnt = 0
#         const max = i ** (1 / 2)
#         let isEnd = false
#         for (let j = 1; j <= max; j++) {
#             if (i % j === 0) {
#                 cnt += 1
#                 if (j ** 2 !== i) {
#                     cnt += 1
#                 }
#                 if (cnt > limit) {
#                     ans += power
#                     isEnd = true
#                     break
#                 }
#             }
#         }
#         if (!isEnd) {
#             ans += cnt
#         }
#     }
    
#     return ans;
# }


### Java

# class Solution {
#     public int solution(int number, int limit, int power) {
#         int ans = 0;
        
#         for (int i = 1; i <= number; i++) {
#             int cnt = 0;
#             int end = (int) Math.sqrt(i);
#             boolean flag = false;
#             for (int j = 1; j <= end; j++) {
#                 if (i % j == 0) {
#                     cnt += 1;
#                     if (Math.pow(j, 2) != i) {
#                         cnt += 1;
#                     }
#                     if (cnt > limit) {
#                         flag = true;
#                         break;
#                     }
#                 }
#             }
            
#             if (flag) {
#                 ans += power;
#             } else {
#                 ans += cnt;   
#             }
#         }
        
#         return ans;
#     }
# }
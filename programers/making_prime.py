# 소수 만들기.  2022-12-08


### Python

def solution(nums):
    global ans
    
    def find(k, cnt, N, tot):
        global ans
        
        if cnt == 3:
            if test(tot):
                ans += 1
            return
        
        for i in range(k, N):
            find(i + 1, cnt + 1, N, tot + nums[i])
    
    
    def test(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    
    ans = 0
    find(0, 0, len(nums), 0)

    return ans


### JS

# function solution(nums) {
#     let ans = 0
    
#     const find = (k, cnt, tot) => {
#         if (cnt === 3) {
#             if (test(tot)) {
#                 ans += 1
#             }
#             return
#         }
        
#         for (let i = k; i < nums.length; i++) {
#             find(i + 1, cnt + 1, tot + nums[i])
#         }
#     }
#     const test = (num) => {
#         for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
#             if (num % i === 0) {
#                 return false
#             }
#         }
#         return true
#     }
    
#     find(0, 0, 0)
#     return ans
# }


### Java

# class Solution {
    
#     public int N;
#     public int ans = 0;
    
#     public void find(int k, int cnt, int tot, int[] nums) {
        
#         if (cnt == 3) {
#             if (test(tot)) {
#                 ans += 1;
#             }
#             return;
#         }
        
#         for (int i = k; i < N; i++) {
#             find(i + 1, cnt + 1, tot + nums[i], nums);
#         }
#     }
    
#     public boolean test(int num) {
        
#         for (int i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
#             if (num % i == 0) {
#                 return false;
#             }
#         }
#         return true;
#     }
    
#     public int solution(int[] nums) {
#         N = nums.length;
        
#         find(0, 0, 0, nums);

#         return ans;
#     }
# }
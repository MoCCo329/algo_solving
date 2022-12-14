# 폰켓몬.  2022-12-14


### Python

def solution(nums):
    
    p_dict = dict()
    N = len(nums) / 2
    tot = 0
    for num in nums:
        if p_dict.get(num, -1) == -1:
            tot += 1
            p_dict[num] = 0
    
    return min(N, tot)


### JS

# function solution(nums) {
#     const pDict = {}
    
#     const N = nums.length / 2
#     let tot = 0
    
#     for (let num of nums) {
#         if (!(num in pDict)) {
#             tot += 1
#             pDict[num] = 0
#         }
#     }
    
#     return Math.min(N, tot)
# }


### Java

# import java.util.HashMap;

# class Solution {
#     public int solution(int[] nums) {
        
#         HashMap hm = new HashMap<Integer, Integer>();
        
#         int N = nums.length / 2;
#         int tot = 0;
        
#         for (int num: nums) {
#             if (hm.get(num) == null) {
#                 tot += 1;
#                 hm.put(num, 0);
#             }
#         }
        
        
#         return Math.min(N, tot);
#     }
# }
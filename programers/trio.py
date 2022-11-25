# 삼총사  2022-11-24


### Python

def solution(number):
    global ans
    
    def dfs(i, cnt, s):
        global ans
        
        if cnt == 3:
            if s == 0:
                ans += 1
            return
        
        for j in range(i, L):
            dfs(j + 1, cnt + 1, s + number[j])


    ans = 0
    L = len(number)
    dfs(0, 0, 0)
    
    return ans


### JS

# function solution(number) {
#     const dfs = (i, cnt, s) => {
#         if (cnt === 3) {
#             if (s === 0) {
#                 ans += 1
#             }
#             return
#         }
        
#         for (let j = i; j < L; j++) {
#             dfs(j + 1, cnt + 1, s + number[j])
#         }
#     }
    
#     let ans = 0
#     let L = number.length
#     dfs(0, 0, 0)
    
#     return ans
# }


### Java

# class Solution {
#     public static int ans;
#     public static int L;
#     public static int[] n;
    
#     public void dfs(int i, int cnt, int s) {
#         if (cnt == 3) {
#             if (s == 0) {
#                 ans += 1;
#             }
#             return;
#         }
        
#         for (int j = i; j < L; j++) {
#             dfs(j + 1, cnt + 1, s + n[j]);
#         }
#     }
    
#     public int solution(int[] number) {
#         n = number;
#         L = number.length;
        
#         dfs(0, 0, 0);
        
#         return ans;
#     }
# }
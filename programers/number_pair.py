# 숫자 짝궁  2022-11-26


### Python

def solution(X, Y):
    ans = ''
    counts = [0] * 10
    ans_counts = [0] * 10
    
    for x in X:
        counts[int(x)] += 1
    for y in Y:
        if counts[int(y)]:
            ans_counts[int(y)] += 1
            counts[int(y)] -= 1
    
    for i in range(9, -1, -1):
        if ans_counts[i]:
            ans += str(i) * ans_counts[i]
    
    if not ans:
        ans = '-1'
    elif ans[0] == ans[-1] == '0':
        ans = '0'
    
    return ans


### JS

# function solution(X, Y) {
#     let ans = ''
#     let counts = [...new Array(10)].map((_, i) => 0)
#     let ans_counts = [...new Array(10)].map((_, i) => 0)
    
#     for (let x of X) {
#         counts[Number(x)] += 1
#     }
#     for (let y of Y) {
#         if (counts[Number(y)]) {
#             ans_counts[Number(y)] += 1
#             counts[Number(y)] -= 1
#         }
#     }
    
#     for (let i = 9; i >= 0; i--) {
#         if (ans_counts[i]) {
#             ans += String(i).repeat(ans_counts[i])
#         }
#     }
    
#     if (!ans) {
#         ans = '-1'
#     } else if (ans.charAt(0) === '0' && ans.length > 1) {
#         ans = '0'
#     }
    
#     return ans
# }


### Java

# import java.util.Arrays;

# class Solution {
#     public String solution(String X, String Y) {
#         String ans = "";
#         int[] counts = new int[10];
#         int[] ans_counts = new int[10];
#         Arrays.fill(counts, 0);
#         Arrays.fill(ans_counts, 0);
        
#         for (int i = 0; i < X.length(); i++) {
#             int cnv = X.charAt(i) - '0';
#             counts[cnv] += 1;
#         }
#         for (int i = 0; i < Y.length(); i++) {
#             int cnv = Y.charAt(i) - '0';
#             if (counts[cnv] > 0) {
#                 ans_counts[cnv] += 1;
#                 counts[cnv] -= 1;
#             }
#         }
        
#         System.out.println(Arrays.toString(ans_counts));
        
#         for (int i = 9; i >= 0; i--) {
#             if (ans_counts[i] > 0) {
#                 ans += String.valueOf(i).repeat(ans_counts[i]);
#             }
#         }
        
#         if (ans == "") {
#             ans = "-1";
#         } else if (ans.charAt(0) == '0') {
#             ans = "0";
#         }
        
#         return ans;
#     }
# }
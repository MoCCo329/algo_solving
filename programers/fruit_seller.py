# 과일 장수  2022-11-25


### Python

def solution(k, m, score):
    ans = 0
    
    score.sort(reverse = True)
    i = -1
    L = len(score)
    while (i + m < L):
        i += m
        ans += score[i] * m
    
    return ans


### JS

# function solution(k, m, score) {
#     let ans = 0;
#     score.sort((a, b) => {
#         return b - a
#     })
    
#     let i = -1
#     const L = score.length
#     while (i + m < L) {
#         i += m
#         ans += score[i] * m
#     }
    
#     return ans
# }


### Java

# import java.util.Arrays;

# class Solution {
#     public int solution(int k, int m, int[] score) {
#         int ans = 0;
#         int L = score.length;
#         int i = L;

#         Arrays.sort(score);
        
#         while (i - m >= 0) {
#             i -= m;
#             ans += score[i] * m;
#         }
        
#         return ans;
#     }
# }
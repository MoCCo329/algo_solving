# 가장 가까운 같은 글자.  2022-12-06


### Python

def solution(s):
    ans = []
    counts = [-1] * 26
    
    for i in range(len(s)):
        if counts[ord(s[i]) - 97] == -1:
            ans.append(-1)
        else:
            ans.append(i - counts[ord(s[i]) - 97])
        counts[ord(s[i]) - 97] = i
    
    return ans


### JS

# function solution(s) {
#     let ans = []
#     const counts = new Array(26);
#     counts.fill(-1)

#     for (let i = 0; i < s.length; i++) {
#         if (counts[s.charCodeAt(i) - 97] === -1) {
#             ans.push(-1)
#         } else {
#             ans.push(i - counts[s.charCodeAt(i) - 97])
#         }
#         counts[s.charCodeAt(i) - 97] = i
#     }
    
#     return ans
# }


### Java

# import java.util.Arrays;

# class Solution {
#     public int[] solution(String s) {
#         int[] counts = new int[26];
#         Arrays.fill(counts, -1);
#         int[] ans = new int[s.length()];
        
#         for (int i = 0; i < s.length(); i++) {
#             if (counts[s.charAt(i) - 'a'] == -1) {
#                 ans[i] = -1;
#             } else {
#                 ans[i] = i - counts[s.charAt(i) - 'a'];
#             }
#             counts[s.charAt(i) - 'a'] = i;
#         }
        
#         return ans;
#     }
# }
# 문자열 나누기  2022-12-01

def solution(s):
    def cut(s):
        start = s[0]
        start_cnt = 1
        non_cnt = 0
        s = s[1:]
        
        for i in range(len(s)):
            if s[i] == start:
                start_cnt += 1
            else:
                non_cnt += 1
            
            if start_cnt == non_cnt:
                s = s[i + 1:]
                break
        else:
            s = ""
        
        return s
    
    ans = 0
    while len(s) > 0:
        s = cut(s)
        ans += 1
    
    return ans


### JS

# function solution(s) {
#     let ans = 0
#     const cut = (s) => {
#         start = s[0]
#         s = s.slice(1)
#         startCnt = 1
#         nonCnt = 0
        
#         for (let i = 0; i < s.length; i++) {
#             if (s[i] === start) startCnt += 1
#             if (s[i] !== start) nonCnt += 1
#             if (startCnt === nonCnt) {
#                 s = s.slice(i + 1)
#                 break
#             }
#         }
#         if (startCnt !== nonCnt) s = ""
        
#         return s
#     }
    
#     while (s.length > 0) {
#         s = cut(s)
#         ans += 1
#     }
    
#     return ans
# }


### Java

# class Solution {
#     public int solution (String s) {
#         int ans = 0;
        
#         while (!s.equals("")) {
#             s = cut(s);
#             ans++;
#         }
#         return ans;
#     }
    
#     public String cut (String s) {
#         char start = s.charAt(0);
#         int startCnt = 1;
#         int nonCnt = 0;
#         int i = 1;
        
#         while (i < s.length() && startCnt != nonCnt) {
#             if (start == s.charAt(i)) startCnt++;
#             else nonCnt++;
#             i++;
#         }
        
#         return s.substring(i);
#     }
# }
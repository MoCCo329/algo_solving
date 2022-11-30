# 3진법 뒤집기  2022-11-30


### Python

def solution(n):
    conv = ""
    while n >= 1:
        n, conv = n // 3, str(n % 3) + conv
    
    return int(conv[::-1], 3)


### JS

# function solution(n) {
#     let conv = n.toString(3)
    
#     return parseInt(conv.split("").reverse().join(""), 3)
# }


### Java

# class Solution {
#     public int solution(int n) {
#         String conv = Integer.toString(n, 3);
        
#         StringBuffer sb = new StringBuffer(conv);
#         int ans = Integer.parseInt(sb.reverse().toString(), 3);
        
#         return ans;
#     }
# }
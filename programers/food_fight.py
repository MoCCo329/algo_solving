# 푸드 파이트 대회  2022-11-22


### Python

def solution(food):
    ans = ''
    
    for i in range(1, len(food)):
        l = food[i] // 2
        ans += str(i) * l
    
    ans = ans + '0' + ans[::-1]
    
    return ans


### JS

# function solution(food) {
#     let answer = '';
    
#     for (let i = 1; i < food.length; i++) {
#         let l = Math.floor(food[i] / 2)
#         answer += String(i).repeat(l)
#     }
    
#     let reversed = ''
#     for (let r of answer) {
#         reversed = r + reversed
#     }
    
#     answer = answer + '0' + reversed
    
#     return answer;
# }


### Java

# class Solution {
#     public String solution(int[] food) {
#         String answer = "";
#         for(int i = 0; i < food.length; i++) {
#             int l = (int) Math.floor(food[i] / 2);
#             answer += String.valueOf(i).repeat(l);
#         }
        
#         String reversed = "";
#         for(int i = 0; i < answer.length(); i++) {
#             reversed = answer.charAt(i) + reversed;
#         }
#         answer = answer + '0' + reversed;
        
#         return answer;
#     }
# }
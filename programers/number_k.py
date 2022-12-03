# k번째수  2022-12-03


### Python

def solution(array, commands):
    ans = []
    
    for command in commands:
        f, t, n = command
        temp = sorted(array[f - 1:t])
        ans.append(temp[n - 1])
    
    return ans


### JS

# function solution(array, commands) {
#     let ans = []
    
#     for (let command of commands) {
#         const [f, t, n] = command
        
#         let temp = array.slice(f - 1, t).sort()
#         ans.push(temp[n - 1])
#     }
    
#     return ans
# }


### Java

# import java.util.Arrays;

# class Solution {
#     public int[] solution(int[] array, int[][] commands) {
#         int[] ans = new int[commands.length];
        
#         for (int i = 0, size = commands.length; i < size; i++) {
#             int f = commands[i][0], t = commands[i][1], n = commands[i][2];
#             int[] temp = new int [t - f + 1];
#             for (int j = 0; j < temp.length; j++) {
#                 temp[j] = array[f + j - 1];
#             }
            
#             Arrays.sort(temp);
#             ans[i] = temp[n - 1];
#         }
        
#         return ans;
#     }
# }
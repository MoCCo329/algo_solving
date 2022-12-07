# 두 개 뽑아서 더하기.  2022-12-07


### Python

def solution(numbers):
    def dfs(k, cnt, tot):
        if cnt == 2:
            ans.add(tot)
            return

        for i in range(k, len(numbers)):
            dfs(i + 1, cnt + 1, tot + numbers[i])
    
    ans = set()
    dfs(0, 0, 0)
    
    return sorted(list(ans))


### JS

# function solution(numbers) {
#     let ans = new Set()
#     const dfs = (k, cnt, tot) => {
#         if (cnt === 2) {
#             ans.add(tot)
#             return
#         }
        
#         for (let i = k; i < numbers.length; i++) {
#             dfs(i + 1, cnt + 1, tot + numbers[i])
#         }
#     }
    
#     dfs(0, 0, 0)
#     ans = [...ans].sort((a, b) => a - b)
    
#     return ans
# }


### Java

# import java.util.HashSet;
# import java.util.Set;
# import java.util.Arrays;

# class Solution {
    
#     public Set<Integer> ansSet = new HashSet<Integer>();
    
#     public void dfs(int k, int cnt, int tot, int[] numbers) {
#         if (cnt == 2) {
#             ansSet.add(tot);
#             return;
#         }
        
#         for (int i = k; i < numbers.length; i++) {
#             dfs(i + 1, cnt + 1, tot + numbers[i], numbers);
#         }
#     }
    
#     public int[] solution(int[] numbers) {
#         dfs(0, 0, 0, numbers);
#         int[] ans = new int[ansSet.size()];
        
#         int i = 0;
#         for (int a: ansSet) {
#             ans[i++] = a;
#         }
#         // Arrays.sort(ans);
        
#         return ans;
#     }
# }
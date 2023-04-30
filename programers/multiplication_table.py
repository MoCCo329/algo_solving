# 억억단을 외우자.  2023-04-30


### Java

# class Solution {
#     public int[] solution(int e, int[] starts) {
        
#         int[] div = new int[e + 1];
        
#         for (int i = 0; i < e + 1; i++) div[i] = 1;
#         for (int i = 2; i < e + 1; i++) for (int j = i; j < e + 1; j += i) div[j] += 1;
#         for (int i = 2; i <= (int) Math.sqrt(e); i++) div[i * i] -= 1;
        
#         int[] divSum = new int[e + 1];
#         divSum[e] = e;
#         for (int i = e - 1; i != 0; i--) {
#             if (div[divSum[i + 1]] <= div[i]) divSum[i] = i;
#             else divSum[i] = divSum[i + 1];
#         }
        
#         int[] ans = new int[starts.length];
#         for (int i = 0; i != starts.length; i++) ans[i] = divSum[starts[i]];
        
#         return ans;
#     }
# }
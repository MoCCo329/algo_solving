# 문자열 내 마음대로 정렬하기.  2022-12-09


### Python

def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))


### JS

# function solution(strings, n) {
#     const ans = strings.sort((a, b) => {
#         if (a[n] === b[n]) {
#             return a > b ? 1 : -1
#         }
#         return a[n].charCodeAt(0) - b[n].charCodeAt(0) > 0 ? 1 : -1
#     })
#     return ans
# }


### Java

# import java.util.Arrays;
# import java.util.Comparator;

# class Solution {
    
#     public String[] solution(String[] strings, int n) {
        
#         Arrays.sort(strings, new Comparator<String>() {
#             public int compare(String i1, String i2) {
#                 if (i1.charAt(n) - i2.charAt(n) == 0) {
#                     return i1.compareTo(i2);
#                 }
#                 return i1.charAt(n) - i2.charAt(n) > 0 ? 1 : -1;
#             }
#         });
        
#         return strings;
#     }
# }
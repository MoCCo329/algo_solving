# 옹알이  2022-11-28


### Python

def solution(babbling):
    ans = 0
    
    for babble in babbling:
        for avail in ["aya", "ye", "woo", "ma"]:
            if avail * 2 not in babble:
                babble = babble.replace(avail, '/')
            else:
                break
        else:
            babble = babble.replace('/', '')
            if not babble:
                ans += 1

    return ans


### JS

# function solution(babbling) {
#     let ans = 0
    
#     for (let babble of babbling) {
#         let chk = false
#         for (let avail of ["aya", "ye", "woo", "ma"]) {
#             if (!babble.includes(avail.repeat(2))) {
#                 babble = babble.replaceAll(avail, '/')
#             } else {
#                 chk = true
#                 break
#             }
#         }
#         if (!chk) {
#             babble = babble.replaceAll('/', '')
#             if (!babble) {
#                 ans += 1
#             }
#         }
#     }
    
#     return ans
# }


### Java

# class Solution {
#     public int solution(String[] babbling) {
#         int ans = 0;
#         String[] avails = {"aya", "ye", "woo", "ma"};
        
#         for (String babble: babbling) {
#             for (String avail: avails) {
#                 if (babble.contains(avail.repeat(2))) break;
#                 babble = babble.replaceAll(avail, "/");
#             }
            
#             babble = babble.replaceAll("/", "");
#             if (babble.equals("")) {
#                 ans += 1;
#             }
#         }
        
#         return ans;
#     }
# }
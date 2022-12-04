# 완주하지 못한 선수  2022-12-04


### Python

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]: return participant[i]
    else:
        return participant[-1]


### JS

# function solution(participant, completion) {
#     participant.sort()
#     completion.sort()
    
#     for (let i = 0, size = completion.length; i < size; i++) {
#         if (participant[i] !== completion[i]) return participant[i]
#     }
#     return participant[participant.length - 1]
# }


### Java

# import java.util.Arrays;

# class Solution {
#     public String solution(String[] participant, String[] completion) {
#         Arrays.sort(participant);
#         Arrays.sort(completion);

#         int i = 0, size = completion.length;
#         while (i < size) {
#             if (!participant[i].equals(completion[i])) return participant[i];
#             i++;
#         }
#         return participant[i];
#     }
# }
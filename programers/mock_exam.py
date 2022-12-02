# 모의고사  2022-12-02


### Python

def solution(answers):
    score = [0] * 3
    
    for i in range(len(answers)):
        if i % 5 + 1 == answers[i]:
            score[0] += 1
        if i % 2:
            if [1, 3, 4, 5][i // 2 % 4] == answers[i]:
                score[1] += 1
        elif answers[i] == 2:
            score[1] += 1
        if [3, 1, 2, 4, 5][i // 2 % 5] == answers[i]:
            score[2] += 1
    
    ans = []
    max_v = -1
    for i in range(3):
        if score[i] > max_v:
            ans = [i + 1]
            max_v = score[i]
        elif score[i] == max_v:
            ans.append(i + 1)

    return ans


### JS

# function solution(answers) {
#     score = [0, 0, 0]
    
#     for (let i = 0; i < answers.length; i++) {
#         // 1번
#         if (i % 5 + 1 == answers[i]) score[0] += 1;
#         // // 2번
#         if (i % 2 == 0) {
#             if (2 == answers[i]) score[1] += 1;
#         } else {
#             if ([1, 3, 4, 5][Math.floor(i / 2) % 4] == answers[i]) score[1] += 1;
#         }
#         // // 3번
#         if ([3, 1, 2, 4, 5][Math.floor(i / 2) % 5] == answers[i]) score[2] += 1;
#     }
    
#     ans = []
#     maxV = -1
#     for (let i = 0; i < 3; i++) {
#         if (maxV < score[i]) {
#             ans = [i + 1]
#             maxV = score[i]
#         } else if (maxV == score[i]) {
#             ans.push(i + 1)
#         }
#     }
    
#     return ans
# }


### Java

# import java.util.ArrayList;
# import java.util.List;

# class Solution {
#     public int[] solution(int[] answers) {
#         int[] score = {0, 0, 0};
#         int[] second = {1, 3, 4, 5};
#         int[] third = {3, 1, 2, 4, 5};
        
#         for (int i = 0; i < answers.length; i++) {
#             // 1번
#             if (i % 5 + 1 == answers[i]) score[0] += 1;
#             // // 2번
#             if (i % 2 == 0) {
#                 if (2 == answers[i]) score[1] += 1;
#             } else {
#                 if (second[(int) Math.floor(i / 2) % 4] == answers[i]) score[1] += 1;
#             }
#             // // 3번
#             if (third[(int) Math.floor(i / 2) % 5] == answers[i]) score[2] += 1;
#         }
        
#         List<Integer> ans = new ArrayList<Integer>();
#         int max_v = score[0];
        
#         ans.add(1);
#         for (int i = 1; i < 3; i++) {
#             if (score[i] > max_v) {
#                 max_v = score[i];
#                 ans.clear();
#                 ans.add(i + 1);
#             } else if (score[i] == max_v) {
#                 ans.add(i + 1);
#             }
#         }
        
#         return ans.stream().mapToInt(i -> i).toArray();
#     }
# }
### Java

# def test(s):
#     m = (len(s) - 1) // 2
#     if m == 0: return 1
    
#     if s[m] == '1':
#         if not test(s[:m]) or not test(s[m + 1:]):
#             return 0
#         else:
#             return 1
    
#     else:
#         if int(s[:m], 2) != 0 or int(s[m + 1:], 2) != 0:
#             return 0
#         else:
#             return 1


# def solution(numbers):
#     ans = []
    
#     for number in numbers:
#         temp = format(number, 'b')
#         k = 1
#         while k - 1 < len(temp): k <<= 1
        
#         if k - 1 == len(temp):
#             pass
#         else:
#             temp = "0" * ((k - 1) - len(temp)) + temp
#         ans.append(test(temp))
    
#     return ans
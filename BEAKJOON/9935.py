# 9935. 문자열 폭발 G4 2022-05-15


s = list(input())
p = list(input())
L = len(s)
pL = len(p)
stack = []
sL = 0

for i in range(L):
    stack.append(s[i])
    sL += 1
    if sL >= pL and stack[-1] == p[-1] and stack[-pL:] == p:
        del stack[-pL:]
        sL -= pL

print("".join(stack) if sL else "FRULA")
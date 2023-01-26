# 1918. 후위 표기식 2023-01-26


infix = input()
postfix = []
s = []
isp = { '(': 0, '+': 1, '-': 1, '*': 2, '/': 2 }

for c in infix:
    if 'A' <= c <= 'Z':
        postfix.append(c)
    elif c == '(':
        s.append(c)
    elif c == ')':
        while s and s[-1] != '(':
            postfix.append(s.pop())
        s.pop()
    else:
        while s and isp[s[-1]] >= isp[c]:
            postfix.append(s.pop())
        s.append(c)
while s:
    postfix.append(s.pop())

print(''.join(postfix))
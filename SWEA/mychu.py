N = int(input())
q = []
p = 1 # 처음 줄 설 사람 번호
my = [0] * (N+1)
cnt = [0] * (N+1) # 몇개 받았는지 저장
m = 0 # 나눠준 개수
v = 0

while m < N:
    q.append(p) # 큐에 처음 사람 번호 넣기
    cnt[p] += 1 # 받은사람 카운트

    v = q.pop(0)
    m += cnt[v]
    my[v] += cnt[v]

    q.append(v)
    cnt[v] += 1
    p += 1

print(f'마지막 사람 : {v}')




N = int(input())
Q = [] # 초기 마이쮸 개수
cnt = [0] * (N+1) # 줄 선 횟수
m = [0] * (N+1) # 받은 초콜릿 수
i = 0 # 나눠준 수
p = 1 # 처음 줄 설 사람 번호

while i < N:
    Q.append(p)
    t = Q.pop(0)
    cnt[t] += 1
    m[t] += cnt[t]
    Q.append(t)

    i += cnt[t]
    p += 1

print(t)
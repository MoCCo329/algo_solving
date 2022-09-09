# 1043. 거짓말  2022-09-09


def test():
    next = False

    for i in range(M):
        if v[i]: continue
        for attendee in parties[i]:
            if listener[attendee]:
                for attendee2 in parties[i]:
                    if listener[attendee2] == 0:
                        next = True
                        listener[attendee2] = 1
                v[i] = 1
                if next:
                    return test()


N, M = map(int, input().split())
listener = [0] * (N + 1)
len_known, *knowns = map(int, input().split())
for known in knowns:
    listener[known] = 1

parties = [list(map(int, input().split()))[1:] for _ in range(M)]
v = [0] * M
test()

ans = 0
for party in parties:
    if party:
        ans += 1
print(M - sum(v))
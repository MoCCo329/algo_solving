T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    v = [1] + [0] * (sum(arr))
    ans = [0]

    for score in arr:
        for i in range(len(ans)):
            temp = ans[i] + score
            if v[temp] == 0:
                ans += [temp]
                v[temp] = 1

    print(f'#{tc} {len(set(ans))}')
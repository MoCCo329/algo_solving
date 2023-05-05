# 16964. DFS 스페셜 저지  2023-05-05


def dfs():
    global cnt, i

    cnt += 1

    a = arr[i]

    while i + 1 < V and arr[i + 1] in adj_list[a]:
        adj_list[a].remove(arr[i + 1])
        adj_list[arr[i + 1]].remove(a)
        i += 1
        dfs()


V = int(input())
adj_list = [set() for _ in range(V + 1)]
for _ in range(V - 1):
    a, b = map(int, input().split())
    adj_list[a].add(b)
    adj_list[b].add(a)

arr = list(map(int, input().split()))

ans = 1
if arr[0] != 1:
    ans = 0
else:
    cnt = 0
    i = 0
    dfs()
    if cnt != V:
        ans = 0

print(ans)
# 14499. 주사위 굴리기 2022-04-10

N, M, j, i, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))


dice = [[0] * 3 for _ in range(4)]
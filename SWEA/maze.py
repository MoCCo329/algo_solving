def f(i, j, direction):
    global top
    i += direction[0]
    j += direction[1]
    temp_stack = [i, j, []]

    for di, dj in didj:
        if 0<=i+di<N and 0<=j+dj<N and maze[i + di][j + dj] == 3: # 끝지점을 만나면 1 반환
            return 1
        if 0<=i+di<N and 0<=j+dj<N and maze[i + di][j + dj] == 0 and [-di, -dj] != direction: # 갈 수 있는 방향이 있고, 그것이 왔던 방향이 아니라면
            temp_stack[2] += [[di, dj]] # 임시 스택에 저장

    if len(temp_stack[2]): # 갈 수 있는 방향이 있으면 스택에 저장
        top += 1
        stack[top] = temp_stack

    if len(stack[top][2]): # 갈 방향이 있으면
        return f(stack[top][0], stack[top][1], stack[top][2].pop()) # 갈 수 있는 길 중 하나를 빼서 함수 실행
    else: # 없으면
        while top > 0 and len(stack[top][2]) == 0: # 방향이 나올때까지 top 감소
            top -= 1
        if top == 0 and len(stack[top][2]) == 0: # 스택이 비면 return 0
            return 0
        else: # 방향이 나오면 함수 실행
            return f(stack[top][0], stack[top][1], stack[top][2].pop())

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    didj = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    stack = [[]] * N**2 # 스택에는 위치 정보[i, j, [갈 수 있는 방향들]]가 담긴다.
    top = 0

    for i in range(N): # stack[0] 찾기 [시작i, j, [갈 수 있는 방향들]]
        for j in range(N):
            if maze[i][j] == 2:
                stack[top] = [i, j, []]
                for di, dj in didj:
                    if 0<=i+di<N and 0<=j+dj<N and maze[i+di][j+dj] == 0:
                        stack[top][2] += [[di, dj]]
        if stack[top]:
            break
    if stack[top][2]:
        ans = f(stack[top][0], stack[top][1], stack[top][2].pop())
    else:
        ans = 0

    print(f'#{tc} {ans}')
# 기둥과 보 설치.  2023-12-03


maps = [[0] * 101 for _ in range(101)]
N = 0


def test():
    global N
    
    for i in range(0, N + 1):
        for j in range(0, N + 1):
            if maps[i][j] == 0:
                continue
            if maps[i][j] & 0b01:
                if not (i == 0 or (maps[i - 1][j] & 0b01) or (0 < j and (maps[i][j - 1] & 0b10)) or (maps[i][j] & 0b10)):
                    return False
            if maps[i][j] & 0b10:
                if not ((maps[i - 1][j] & 0b01) or (j < N and (maps[i - 1][j + 1] & 0b01)) or
                        ((0 < j and (maps[i][j - 1] & 0b10)) and (j < N and (maps[i][j + 1] & 0b10)))):
                    return False
    
    return True


def solution(n, build_frame):
    global N
    N = n;
    
    for frame in build_frame:
        type = 0b01 if frame[2] == 0 else 0b10
        i, j = frame[1], frame[0]
        if frame[3] == 0:  # 삭제
            maps[i][j] -= type
            if not test():
                maps[i][j] |= type
        else:  # 삽입
            maps[i][j] |= type
            if not test():
                maps[i][j] -= type

    ans = []
    for i in range(0, N + 1):
        for j in range(0, N + 1):
            if maps[i][j] & 0b01:
                ans.append([j, i, 0])
            if maps[i][j] & 0b10:
                ans.append([j, i, 1])
    ans.sort()
    
    return ans
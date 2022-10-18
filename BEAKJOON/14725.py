# 14725 개미굴.  2022-10-18


def print_food(path):
    temp = sd
    for floor in path:
        temp = temp[floor]
    keys = list(temp['.'])
    keys.sort()
    print('--' * (len(path) - 1) + path[-1])
    for key in keys:
        print_food(path + [key])


sd = dict()
sd['.'] = set()
N = int(input())
for _ in range(N):
    depth, *floors = input().split()
    temp = sd
    for floor in floors:
        temp['.'].add(floor)
        if temp.get(floor, 0):
            temp = temp[floor]
        else:
            temp[floor] = dict()
            temp = temp[floor]
            temp['.'] = set()

keys = list(sd['.'])
keys.sort()
for key in keys:
    print_food([key])
# 호텔 방 배정.  2023-09-08


import sys


sys.setrecursionlimit(200001)


def find(i):
    global vis, next_room
    if i not in next_room:
        next_room[i] = i
    if next_room[i] in vis:
        next_room[i] = find(next_room[i] + 1)
    
    return next_room[i]


def solution(k, room_number):
    global vis, next_room
    
    vis = set()
    next_room = dict()
    
    ans = []
    for room in room_number:
        i = find(room)
        vis.add(i)
        ans.append(i)
    
    return ans

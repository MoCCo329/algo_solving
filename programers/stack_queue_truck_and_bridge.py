# 다리를 지나는 트럭  2022-07-27


def solution(bridge_length, weight, truck_weights):
    total = truck_weights[0]
    q = [(0, 0)]
    i = 1
    t = 1
    while q or i < len(truck_weights):
        if t - q[0][1] == bridge_length:
            total -= truck_weights[q.pop(0)[0]]
        if i < len(truck_weights) and bridge_length >= len(q) and total + truck_weights[i] <= weight:
            total += truck_weights[i]
            q.append((i, t))
            i += 1
        t += 1

    return t
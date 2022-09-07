# [1차] 캐시 2018 KAKAO BLIND RECRUITMENT 2022-09-07


from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    size_now = 0

    ans = 0
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache:
            ans += 1
            cache.remove(city)
            cache.append(city)
        else:
            ans += 5
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)

    return ans
# 베스트 엘범  2022-07-26


def solution(genres, plays):
    N = len(genres)
    dic = dict()
    dic_cnt = dict()
    zipped_list = []
    for i in range(N):
        temp = dic.get(genres[i], -1)
        if temp != -1:
            dic[genres[i]] += plays[i]
            if dic_cnt[genres[i]] < 2:
                dic_cnt[genres[i]] += 1
        else:
            dic[genres[i]] = plays[i]
            dic_cnt[genres[i]] = 1
        zipped_list.append([i, genres[i]])

    zipped_list.sort(key=lambda x: (-dic[x[1]], -plays[x[0]], x[0]))

    ans = []
    for i in range(N):
        idx, genre = zipped_list[i]
        if dic_cnt[genre]:
            ans.append(idx)
            dic_cnt[genre] -= 1
    return ans
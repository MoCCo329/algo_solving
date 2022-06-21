# 신고 결과 받기 2022 KAKAO BLIND RECRUITMENT  2022-06-21


def solution(id_list, report, k):
    answer = []
    ans_dict = {id: 0 for id in id_list}
    rep_dict = dict()
    
    for rep in report:
        reporter, reportee = rep.split()
        if rep_dict.get(reportee, -1) == -1:
            rep_dict[reportee] = [reporter]
        else:
            if reporter not in rep_dict[reportee]:
                rep_dict[reportee].append(reporter)
    
    for key, values in rep_dict.items():
        if len(values) >= k:
            for id in values:
                ans_dict[id] += 1
    
    for key, value in ans_dict.items():
        answer.append(value)
    
    return answer
# 메뉴 리뉴얼 2021 KAKAO BLIND RECRUITMENT  2022-09-15


def solution(orders, course):
    def dfs(j, k, menu):  # j번째 주문, k번째 원소 진행중, menu 선택함
        if len(menu) in course:
            temp = ''.join(sorted(menu, key=lambda x: ord(x)))
            if menu_dict[len(menu)].get(temp, 0):
                menu_dict[len(menu)][temp] += 1
            else:
                menu_dict[len(menu)][temp] = 1
        elif len(menu) > course[-1]:
            return

        for i in range(k, len(orders[j])):
            dfs(j, i + 1, menu + [orders[j][i]])

    menu_dict = {cnt: dict() for cnt in course}
    for i in range(len(orders)):
        dfs(i, 0, [])

    ans = []
    for length, sum_dict in menu_dict.items():
        temp = []
        max_v = 0
        for set_menu, cnt in sum_dict.items():
            if max_v < cnt:
                temp = [set_menu]
                max_v = cnt
            elif max_v == cnt:
                temp.append(set_menu)
        if max_v > 1:
            ans.extend(temp)

    ans.sort()
    return ans
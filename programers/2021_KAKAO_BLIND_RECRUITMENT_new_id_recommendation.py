# 신규 아이디 추천 2021 KAKAO BLIND RECRUITMENT  2022-09-08


def solution(new_id):
    # 1.
    new_id = new_id.lower()
    # 2.
    new_id_list = []
    for cha in new_id:
        cha_ord = ord(cha)
        if cha.isalpha() or cha_ord == ord('.') or cha_ord == ord('-') or cha_ord == ord('_') or ord(
                '0') <= cha_ord <= ord('9'):
            new_id_list.append(cha)
    new_id = ''.join(new_id_list)
    # 3.
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # 4.
    new_id = new_id.strip('.')
    # 5.
    if new_id == '':
        new_id = 'a'
    # 6.
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:14]
    # 7.
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1] * (3 - len(new_id))

    return new_id
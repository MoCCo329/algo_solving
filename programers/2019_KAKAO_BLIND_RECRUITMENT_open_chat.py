# 오픈채팅방 2019 KAKAO BLIND RECRUITMENT  2022-09-14


def solution(record):
    user_dict = dict()

    for rec in record:
        status, *user_id = rec.split()
        if status != 'Leave':
            user_dict[user_id[0]] = user_id[1]

    ans = []
    for rec in record:
        status, *user_id = rec.split()
        if status == 'Enter':
            ans.append(f'{user_dict[user_id[0]]}님이 들어왔습니다.')
        elif status == 'Leave':
            ans.append(f'{user_dict[user_id[0]]}님이 나갔습니다.')

    return ans
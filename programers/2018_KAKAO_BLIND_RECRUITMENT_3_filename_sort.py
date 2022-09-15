# [3차] 파일명 정렬 2018 KAKAO BLIND RECRUITMENT  2022-09-15


def solution(files):
    new_files = []
    for i in range(len(files)):
        file = files[i]
        number = ''
        start = 0
        for j in range(len(file)):
            try:
                num = int(file[j])
                number += file[j]
                if len(number) == 1:
                    start = j
                j += 1
            except:
                if number:
                    break
                else:
                    j += 1
                    continue
        head = file[:start]
        tail = file[j:]
        new_files.append((head, number, tail, i))

    new_files.sort(key=lambda x: (x[0].lower(), int(x[1]), x[3]))

    return [''.join(file[:3]) for file in new_files]
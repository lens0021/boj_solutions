# https://programmers.co.kr/learn/courses/30/lessons/42888


MSG_ENTER = "%s님이 들어왔습니다."
MSG_LEAVE = "%s님이 나갔습니다."


def solution(record):
    nickname = {}
    for row in record:
        words = row.split()
        if words[0] == 'Enter':
            nickname[words[1]] = words[2]
        elif words[0] == 'Change':
            nickname[words[1]] = words[2]
        elif words[0] == 'Leave':
            pass

    answer = []
    for row in record:
        words = row.split()
        if words[0] == 'Enter':
            answer.append(MSG_ENTER % nickname[words[1]])
        elif words[0] == 'Change':
            pass
        elif words[0] == 'Leave':
            answer.append(MSG_LEAVE % nickname[words[1]])

    return answer

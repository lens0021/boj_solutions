# https://programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    completionMap = {}

    for player in completion:
        if player not in completionMap:
            completionMap[player] = 1
        else:
            completionMap[player] += 1

    for player in participant:
        if player not in completionMap or completionMap[player] == 0:
            return player
        elif completionMap[player] > 0:
            completionMap[player] -= 1

    return ''

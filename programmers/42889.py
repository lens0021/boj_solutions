# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stuck_stage_of_players):
    stage = [0] * (N+1)
    for s in stuck_stage_of_players:
        stage[s-1] += 1

    rate = [0] * N
    for s in range(N):
        total = sum(stage[s:])
        if total == 0:
            rate[s] = 0
        else:
            rate[s] = stage[s] / total

    return sorted(list(range(1, N+1)), key=lambda n: rate[n-1], reverse=True)

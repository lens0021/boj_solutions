# https://www.acmicpc.net/problem/14924

(speed_of_trains, speed_of_fly, distance) = map(int, input().split(' '))
print(distance * speed_of_fly // (2 * speed_of_trains))

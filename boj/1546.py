# https://www.acmicpc.net/problem/1546

num = int(input())
scores = list(map(int, input().split(' ')))
max_score = max(scores)

print(sum(scores)/num/max_score*100)

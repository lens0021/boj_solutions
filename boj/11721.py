# https://www.acmicpc.net/problem/11721
s = input()

print('\n'.join(
    s[i:i+10]
    for i in range(0, len(s)+1, 10)
))

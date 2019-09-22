# https://www.acmicpc.net/problem/2739

base = int(input())
print('\n'.join(
    f'{base} * {n} = {base*n}'
    for n in range(1, 10)
))

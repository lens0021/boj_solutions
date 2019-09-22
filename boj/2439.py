# https://www.acmicpc.net/problem/2439

width = int(input())
print(
    '\n'.join(
        ('*' * (num)).rjust(width)
        for num in range(1, width+1)
    )
)

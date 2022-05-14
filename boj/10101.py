# https://www.acmicpc.net/problem/10101

a, b, c = sorted(map(int, [input() for _ in range(3)]))

if a == b == c == 60:
    print('Equilateral')
elif a + b + c == 180:
    if a == b or b == c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')

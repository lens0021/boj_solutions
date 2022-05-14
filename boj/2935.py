# https://www.acmicpc.net/problem/2935
a = len(input())
operator = input()
b = len(input())
if a > b:
    a, b = b, a

if operator == '*':
    print(f'1{"0"*(a+b-2)}')
else:
    if a == b:
        print(f'2{"0"*(a-1)}')
    else:
        print('1', end='')
        print('0' * (b - a - 1), end='')
        print('1', end='')
        print('0' * (a - 1))

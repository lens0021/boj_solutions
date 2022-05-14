# https://www.acmicpc.net/problem/5355

for _ in range(int(input())):
    tokens = input().split()
    num = float(tokens[0])

    for operator in tokens[1:]:
        if operator == '@':
            num = num * 3
        elif operator == '%':
            num = num + 5
        else:
            num = num - 7

    print('%.2f' % num)

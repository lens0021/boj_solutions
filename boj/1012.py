# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(150000)

DEBUG = False


def log(msg='', end='\n'):
    if DEBUG:
        print(msg, end=end)


def find_cabbage(field):
    x, y = 0, 0
    while y < len(field[0]):
        if field[x][y]:
            log(f'There is a cabbage at {(x, y)}')
            return (x, y)

        if x < len(field)-1:
            x += 1
        else:
            x = 0
            y += 1

    log(f'There is no cabbage')
    # print_field(field)
    return False


def is_cabbage(field, x, y):
    if x < 0 or y < 0 or x >= len(field) or y >= len(field[0]):
        return False

    return field[x][y]


def bucket_tool(field, x, y):
    # log(f'Use bucket at ({x}, {y})')
    if is_cabbage(field, x, y):
        field[x][y] = False

        bucket_tool(field, x+1, y)
        bucket_tool(field, x-1, y)
        bucket_tool(field, x, y+1)
        bucket_tool(field, x, y-1)


def get_number_of_areas(field):
    number_of_worms = 0

    area = find_cabbage(field)
    while area is not False:
        log(f'The {number_of_worms+1}th worm:')
        bucket_tool(field, *area)
        number_of_worms += 1
        area = find_cabbage(field)

    return number_of_worms


def print_field(field):
    for row in field:
        for cell in row:
            if cell:
                log('#', end=' ')
            else:
                log('.', end=' ')
        log()


number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    width, height, number_of_cabbages = map(int, input().split())
    field = list([False for _ in range(height)] for _ in range(width))

    for _ in range(number_of_cabbages):
        x, y = map(int, input().split())
        field[x][y] = True

    print_field(field)

    print(get_number_of_areas(field))

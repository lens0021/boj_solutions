# https://www.acmicpc.net/problem/1110
def operation(num):
    return num % 10 * 10 + (num // 10 + num % 10) % 10


original_num = int(input())
num = operation(original_num)
ctr = 1
while num != original_num:
    num = operation(num)
    ctr += 1

print(ctr)
